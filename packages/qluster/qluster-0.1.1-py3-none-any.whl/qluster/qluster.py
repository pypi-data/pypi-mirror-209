import os
import numpy as np
import precession
from tqdm import tqdm
import tqdm_pathos
import h5ify


def sample_powerlaw(s, lo, hi, n=1):

    if s == -1:
        return np.exp(np.random.uniform(np.log(lo), np.log(hi), n))

    else:
        return (
            np.random.rand(n) * (hi**(s + 1) - lo**(s + 1)) + lo**(s + 1)
            )**(1 / (s + 1))


def pairing(data, alpha, beta):

    m = data[:, 0]

    p1 = (m > min(m)) * m**alpha
    ind1 = np.random.choice(m.size, p=p1/np.sum(p1))

    p2 = (m < m[ind1]) * m**beta
    ind2 = np.random.choice(m.size, p=p2/np.sum(p2))

    assert ind1 != ind2
    assert m[ind1] > m[ind2]

    bh1 = data[ind1]
    bh2 = data[ind2]
    rest = np.delete(data, (ind1, ind2), axis=0)

    return bh1, bh2, rest


def remnant(theta1, theta2, deltaphi, M, q, chi1, chi2):

    mf = M * precession.remnantmass(theta1, theta2, q, chi1, chi2)
    chif = precession.remnantspin(theta1, theta2, deltaphi, q, chi1, chi2)
    vf = precession.remnantkick(
        theta1, theta2, deltaphi, q, chi1, chi2, kms=True,
        )

    return np.squeeze((mf, chif, vf))


def check_file(file):

    if file[-3:] != '.h5':
        file += '.h5'

    assert not os.path.isfile(file)

    return file


def cluster(
    vesc,
    n_1g, gamma, mmin, mmax, chimin, chimax,
    alpha, beta,
    file='./cluster.h5',
    seed=None,
    ):

    file = check_file(file)

    np.random.seed(seed)

    masses = sample_powerlaw(gamma, mmin, mmax, n_1g)
    spins = np.random.uniform(chimin, chimax, n_1g)
    generations = np.ones(n_1g)
    data = np.transpose([masses, spins, generations])
    mergers = []

    pbar = tqdm(total=len(data)-1, desc='Mergers')

    while len(data) > 1:
        bh1, bh2, data = pairing(data, alpha, beta)
        m1, chi1, gen1 = bh1
        m2, chi2, gen2 = bh2
        q = m2 / m1
        M = m1 + m2

        theta1, theta2 = np.arccos(np.random.uniform(-1, 1, 2))
        phi1, phi2 = np.random.uniform(0, 2*np.pi, 2)
        deltaphi = phi2 - phi1

        mf, chif, vf = remnant(theta1, theta2, deltaphi, M, q, chi1, chi2)
        genf = gen1 + gen2

        if   gen1 == 1 and gen2 == 1: generation = 11
        elif gen1 == 1 and gen2 == 2: generation = 12
        elif gen1 == 2 and gen2 == 1: generation = 12
        elif gen1 == 2 and gen2 == 2: generation = 22
        else:                         generation = 0

        merger = [
            M, q, chi1, chi2, theta1, theta2, deltaphi, generation,
            mf, chif, vf, genf,
            ]
        mergers.append(merger)

        if vf < vesc:
            data = np.append(data, [[mf, chif, genf]], axis=0)
            pbar.update(1)
        else:
            pbar.update(2)

    pbar.close()

    attrs = {
        'vesc': vesc,
        'n_1g': n_1g,
        'gamma': gamma,
        'mmin': mmin,
        'mmax': mmax,
        'chimin': chimin,
        'chimax': chimax,
        'alpha': alpha,
        'beta': beta,
        'n_mergers': len(mergers),
        'seed': seed,
         }

    pars = (
        'M', 'q', 'chi1', 'chi2', 'theta1', 'theta2', 'deltaphi', 'generation',
        'mf', 'chif', 'vf', 'genf',
        )
    data = {par: val for par, val in zip(pars, np.transpose(mergers))}

    h5ify.save(
        file, {'attrs': attrs, **data}, compression='gzip', compression_opts=9,
        )


def clusters(
    n_clusters, delta, vescmin, vescmax,
    n_1g, gamma, mmin, mmax, chimin, chimax,
    alpha, beta,
    file='./cluster.h5',
    seed=None,
    n_cpus=1,
    group_clusters=True,
    keep_clusters=False,
    ):

    file = check_file(file)
    
    np.random.seed(seed)

    print('Clusters')

    # delta function escape speeds
    if delta is None and vescmin == vescmax:
        vescs = vescmin * np.ones(n_clusters)
    # power law escape speeds
    else:
        vescs = sample_powerlaw(delta, vescmin, vescmax, n_clusters)

    if seed is None:
        seeds = [None] * n_clusters
    else:
        seeds = list(range(seed+1, seed+1+n_clusters))

    def single(ind, vesc):

        return cluster(
            vesc,
            n_1g, gamma, mmin, mmax, chimin, chimax,
            alpha, beta,
            file=f'{file.split(".h5")[0]}_{ind}.h5',
            seed=seeds[ind],
            )

    if n_cpus > 1:
        _ = tqdm_pathos.starmap(single, enumerate(vescs), n_cpus=n_cpus)
    else:
        _ = list(tqdm(map(single, range(n_clusters), vescs), total=n_clusters))

    if group_clusters:
        attrs = {
            'n_clusters':  n_clusters,
            'delta': delta,
            'vescmin': vescmin,
            'vescmax': vescmax,
            'n_1g': n_1g,
            'gamma': gamma,
            'mmin': mmin,
            'mmax': mmax,
            'chimin': chimin,
            'chimax': chimax,
            'alpha': alpha,
            'beta': beta,
            'seed': seed,
            }
        consolidate(file, attrs, keep_clusters)


def consolidate(file, attrs, keep_clusters=False):

    file = check_file(file)

    print('Consolidating')

    h5ify.save(file, {'attrs': attrs})

    for ind in tqdm(range(attrs['n_clusters'])):
        data = {str(ind): h5ify.load(f'{file.split(".h5")[0]}_{ind}.h5')}
        h5ify.save(file, data, compression='gzip', compression_opts=9)

    if not keep_clusters:
        for ind in range(attrs['n_clusters']):
            os.system(f'rm {file.split(".h5")[0]}_{ind}.h5')


if __name__ == '__main__':
    
    pass

