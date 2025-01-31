# Full configuration interaction theory




## Slater determinants as basis states, Repetition
The simplest possible choice for many-body wavefunctions are **product** wavefunctions.
That is

$$
\Psi(x_1, x_2, x_3, \ldots, x_A) \approx \phi_1(x_1) \phi_2(x_2) \phi_3(x_3) \ldots
$$

because we are really only good  at thinking about one particle at a time. Such 
product wavefunctions, without correlations, are easy to 
work with; for example, if the single-particle states $\phi_i(x)$ are orthonormal, then 
the product wavefunctions are easy to orthonormalize.   

Similarly, computing matrix elements of operators are relatively easy, because the 
integrals factorize.


The price we pay is the lack of correlations, which we must build up by using many, many product 
wavefunctions. (Thus we have a trade-off: compact representation of correlations but 
difficult integrals versus easy integrals but many states required.)




## Slater determinants as basis states, repetition
Because we have fermions, we are required to have antisymmetric wavefunctions, e.g.

$$
\Psi(x_1, x_2, x_3, \ldots, x_A) = - \Psi(x_2, x_1, x_3, \ldots, x_A)
$$

etc. This is accomplished formally by using the determinantal formalism

$$
\Psi(x_1, x_2, \ldots, x_A) 
= \frac{1}{\sqrt{A!}} 
\det \left | 
\begin{array}{cccc}
\phi_1(x_1) & \phi_1(x_2) & \ldots & \phi_1(x_A) \\
\phi_2(x_1) & \phi_2(x_2) & \ldots & \phi_2(x_A) \\
 \vdots & & &  \\
\phi_A(x_1) & \phi_A(x_2) & \ldots & \phi_A(x_A) 
\end{array}
\right |
$$

Product wavefunction + antisymmetry = Slater determinant.




## Slater determinants as basis states

$$
\Psi(x_1, x_2, \ldots, x_A) 
= \frac{1}{\sqrt{A!}} 
\det \left | 
\begin{array}{cccc}
\phi_1(x_1) & \phi_1(x_2) & \ldots & \phi_1(x_A) \\
\phi_2(x_1) & \phi_2(x_2) & \ldots & \phi_2(x_A) \\
 \vdots & & &  \\
\phi_A(x_1) & \phi_A(x_2) & \ldots & \phi_A(x_A) 
\end{array}
\right |
$$

Properties of the determinant (interchange of any two rows or 
any two columns yields a change in sign; thus no two rows and no 
two columns can be the same) lead to the Pauli principle:

* No two particles can be at the same place (two columns the same); and

* No two particles can be in the same state (two rows the same).





## Slater determinants as basis states
As a practical matter, however, Slater determinants beyond $N=4$ quickly become 
unwieldy. Thus we turn to the **occupation representation** or **second quantization** to simplify calculations. 

The occupation representation or number representation, using fermion **creation** and **annihilation** 
operators, is compact and efficient. It is also abstract and, at first encounter, not easy to 
internalize. It is inspired by other operator formalism, such as the ladder operators for 
the harmonic oscillator or for angular momentum, but unlike those cases, the operators **do not have coordinate space representations**.

Instead, one can think of fermion creation/annihilation operators as a game of symbols that 
compactly reproduces what one would do, albeit clumsily, with full coordinate-space Slater 
determinants.




## Quick repetition of the occupation representation
We start with a set of orthonormal single-particle states $\{ \phi_i(x) \}$. 
(Note: this requirement, and others, can be relaxed, but leads to a 
more involved formalism.) **Any** orthonormal set will do. 

To each single-particle state $\phi_i(x)$ we associate a creation operator 
$\hat{a}^\dagger_i$ and an annihilation operator $\hat{a}_i$. 

When acting on the vacuum state $| 0 \rangle$, the creation operator $\hat{a}^\dagger_i$ causes 
a particle to occupy the single-particle state $\phi_i(x)$:

$$
\phi_i(x) \rightarrow \hat{a}^\dagger_i |0 \rangle
$$

## Quick repetition  of the occupation representation
But with multiple creation operators we can occupy multiple states:

$$
\phi_i(x) \phi_j(x^\prime) \phi_k(x^{\prime \prime}) 
\rightarrow \hat{a}^\dagger_i \hat{a}^\dagger_j \hat{a}^\dagger_k |0 \rangle.
$$

Now we impose antisymmetry, by having the fermion operators satisfy  **anticommutation relations**:

$$
\hat{a}^\dagger_i \hat{a}^\dagger_j + \hat{a}^\dagger_j \hat{a}^\dagger_i
= [ \hat{a}^\dagger_i ,\hat{a}^\dagger_j ]_+ 
= \{ \hat{a}^\dagger_i ,\hat{a}^\dagger_j \} = 0
$$

so that

$$
\hat{a}^\dagger_i \hat{a}^\dagger_j = - \hat{a}^\dagger_j \hat{a}^\dagger_i
$$

## Quick repetition  of the occupation representation
Because of this property, automatically $\hat{a}^\dagger_i \hat{a}^\dagger_i = 0$, 
enforcing the Pauli exclusion principle.  Thus when writing a Slater determinant 
using creation operators,

$$
\hat{a}^\dagger_i \hat{a}^\dagger_j \hat{a}^\dagger_k \ldots |0 \rangle
$$

each index $i,j,k, \ldots$ must be unique.

For some relevant exercises with solutions see chapter 8 of [Lecture Notes in Physics, volume 936](http://www.springer.com/us/book/9783319533353).





## Full Configuration Interaction Theory
We have defined the ansatz for the ground state as

$$
|\Phi_0\rangle = \left(\prod_{i\le F}\hat{a}_{i}^{\dagger}\right)|0\rangle,
$$

where the index $i$ defines different single-particle states up to the Fermi level. We have assumed that we have $N$ fermions. 
A given one-particle-one-hole ($1p1h$) state can be written as

$$
|\Phi_i^a\rangle = \hat{a}_{a}^{\dagger}\hat{a}_i|\Phi_0\rangle,
$$

while a $2p2h$ state can be written as

$$
|\Phi_{ij}^{ab}\rangle = \hat{a}_{a}^{\dagger}\hat{a}_{b}^{\dagger}\hat{a}_j\hat{a}_i|\Phi_0\rangle,
$$

and a general $NpNh$ state as

$$
|\Phi_{ijk\dots}^{abc\dots}\rangle = \hat{a}_{a}^{\dagger}\hat{a}_{b}^{\dagger}\hat{a}_{c}^{\dagger}\dots\hat{a}_k\hat{a}_j\hat{a}_i|\Phi_0\rangle.
$$

## Full Configuration Interaction Theory
We can then expand our exact state function for the ground state 
as

$$
|\Psi_0\rangle=C_0|\Phi_0\rangle+\sum_{ai}C_i^a|\Phi_i^a\rangle+\sum_{abij}C_{ij}^{ab}|\Phi_{ij}^{ab}\rangle+\dots
=(C_0+\hat{C})|\Phi_0\rangle,
$$

where we have introduced the so-called correlation operator

$$
\hat{C}=\sum_{ai}C_i^a\hat{a}_{a}^{\dagger}\hat{a}_i  +\sum_{abij}C_{ij}^{ab}\hat{a}_{a}^{\dagger}\hat{a}_{b}^{\dagger}\hat{a}_j\hat{a}_i+\dots
$$

Since the normalization of $\Psi_0$ is at our disposal and since $C_0$ is by hypothesis non-zero, we may arbitrarily set $C_0=1$ with 
corresponding proportional changes in all other coefficients. Using this so-called intermediate normalization we have

$$
\langle \Psi_0 | \Phi_0 \rangle = \langle \Phi_0 | \Phi_0 \rangle = 1,
$$

resulting in

$$
|\Psi_0\rangle=(1+\hat{C})|\Phi_0\rangle.
$$

## Full Configuration Interaction Theory
We rewrite

$$
|\Psi_0\rangle=C_0|\Phi_0\rangle+\sum_{ai}C_i^a|\Phi_i^a\rangle+\sum_{abij}C_{ij}^{ab}|\Phi_{ij}^{ab}\rangle+\dots,
$$

in a more compact form as

$$
|\Psi_0\rangle=\sum_{PH}C_H^P\Phi_H^P=\left(\sum_{PH}C_H^P\hat{A}_H^P\right)|\Phi_0\rangle,
$$

where $H$ stands for $0,1,\dots,n$ hole states and $P$ for $0,1,\dots,n$ particle states. 
Our requirement of unit normalization gives

$$
\langle \Psi_0 | \Phi_0 \rangle = \sum_{PH}|C_H^P|^2= 1,
$$

and the energy can be written as

$$
E= \langle \Psi_0 | \hat{H} |\Phi_0 \rangle= \sum_{PP'HH'}C_H^{*P}\langle \Phi_H^P | \hat{H} |\Phi_{H'}^{P'} \rangle C_{H'}^{P'}.
$$

## Full Configuration Interaction Theory
Normally

$$
E= \langle \Psi_0 | \hat{H} |\Phi_0 \rangle= \sum_{PP'HH'}C_H^{*P}\langle \Phi_H^P | \hat{H} |\Phi_{H'}^{P'} \rangle C_{H'}^{P'},
$$

is solved by diagonalization setting up the Hamiltonian matrix defined by the basis of all possible Slater determinants. A diagonalization
<!-- to do: add text about Rayleigh-Ritz -->
is equivalent to finding the variational minimum   of

$$
\langle \Psi_0 | \hat{H} |\Phi_0 \rangle-\lambda \langle \Psi_0 |\Phi_0 \rangle,
$$

where $\lambda$ is a variational multiplier to be identified with the energy of the system.
The minimization process results in

2
3
 
<
<
<
!
!
M
A
T
H
_
B
L
O
C
K

$$
\sum_{P'H'}\left\{\delta[C_H^{*P}]\langle \Phi_H^P | \hat{H} |\Phi_{H'}^{P'} \rangle C_{H'}^{P'}+
C_H^{*P}\langle \Phi_H^P | \hat{H} |\Phi_{H'}^{P'} \rangle \delta[C_{H'}^{P'}]-
\lambda( \delta[C_H^{*P}]C_{H'}^{P'}+C_H^{*P}\delta[C_{H'}^{P'}]\right\} = 0.
$$

Since the coefficients $\delta[C_H^{*P}]$ and $\delta[C_{H'}^{P'}]$ are complex conjugates it is necessary and sufficient to require the quantities that multiply with $\delta[C_H^{*P}]$ to vanish.






## Full Configuration Interaction Theory

This leads to

$$
\sum_{P'H'}\langle \Phi_H^P | \hat{H} |\Phi_{H'}^{P'} \rangle C_{H'}^{P'}-\lambda C_H^{P}=0,
$$

for all sets of $P$ and $H$.

If we then multiply by the corresponding $C_H^{*P}$ and sum over $PH$ we obtain

$$
\sum_{PP'HH'}C_H^{*P}\langle \Phi_H^P | \hat{H} |\Phi_{H'}^{P'} \rangle C_{H'}^{P'}-\lambda\sum_{PH}|C_H^P|^2=0,
$$

leading to the identification $\lambda = E$. This means that we have for all $PH$ sets

<!-- Equation labels as ordinary links -->
<div id="eq:fullci"></div>

$$
\begin{equation}
\sum_{P'H'}\langle \Phi_H^P | \hat{H} -E|\Phi_{H'}^{P'} \rangle = 0. \label{eq:fullci} \tag{1}
\end{equation}
$$

## Full Configuration Interaction Theory
An alternative way to derive the last equation is to start from

$$
(\hat{H} -E)|\Psi_0\rangle = (\hat{H} -E)\sum_{P'H'}C_{H'}^{P'}|\Phi_{H'}^{P'} \rangle=0,
$$

and if this equation is successively projected against all $\Phi_H^P$ in the expansion of $\Psi$, then the last equation on the previous slide
results.   As stated previously, one solves this equation normally by diagonalization. If we are able to solve this equation exactly (that is
numerically exactly) in a large Hilbert space (it will be truncated in terms of the number of single-particle states included in the definition
of Slater determinants), it can then serve as a benchmark for other many-body methods which approximate the correlation operator
$\hat{C}$.





## Example of a Hamiltonian matrix
Suppose, as an example, that we have six fermions below the Fermi level.
This means that we can make at most $6p-6h$ excitations. If we have an infinity of single particle states above the Fermi level, we will obviously have an infinity of say $2p-2h$ excitations. Each such way to configure the particles is called a **configuration**. We will always have to truncate in the basis of single-particle states.
This gives us a finite number of possible Slater determinants. Our Hamiltonian matrix would then look like (where each block can have a large dimensionalities):

<table border="1">
<thead>
<tr><th align="center">       </th> <th align="center">$0p-0h$</th> <th align="center">$1p-1h$</th> <th align="center">$2p-2h$</th> <th align="center">$3p-3h$</th> <th align="center">$4p-4h$</th> <th align="center">$5p-5h$</th> <th align="center">$6p-6h$</th> </tr>
</thead>
<tbody>
<tr><td align="center">   $0p-0h$    </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   0          </td> <td align="center">   0          </td> <td align="center">   0          </td> <td align="center">   0          </td> </tr>
<tr><td align="center">   $1p-1h$    </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   0          </td> <td align="center">   0          </td> <td align="center">   0          </td> </tr>
<tr><td align="center">   $2p-2h$    </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   0          </td> <td align="center">   0          </td> </tr>
<tr><td align="center">   $3p-3h$    </td> <td align="center">   0          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   0          </td> </tr>
<tr><td align="center">   $4p-4h$    </td> <td align="center">   0          </td> <td align="center">   0          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> </tr>
<tr><td align="center">   $5p-5h$    </td> <td align="center">   0          </td> <td align="center">   0          </td> <td align="center">   0          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> </tr>
<tr><td align="center">   $6p-6h$    </td> <td align="center">   0          </td> <td align="center">   0          </td> <td align="center">   0          </td> <td align="center">   0          </td> <td align="center">   x          </td> <td align="center">   x          </td> <td align="center">   x          </td> </tr>
</tbody>
</table>
with a two-body force. Why are there non-zero blocks of elements?




## Example of a Hamiltonian matrix with a Hartree-Fock basis
If we use a Hartree-Fock basis, this corresponds to a particular unitary transformation where matrix elements of the type $\langle 0p-0h \vert \hat{H} \vert 1p-1h\rangle =\langle \Phi_0 | \hat{H}|\Phi_{i}^{a}\rangle=0$ and our Hamiltonian matrix becomes 

<table border="1">
<thead>
<tr><th align="center">       </th> <th align="center">  $0p-0h$  </th> <th align="center">  $1p-1h$  </th> <th align="center">  $2p-2h$  </th> <th align="center">  $3p-3h$  </th> <th align="center">  $4p-4h$  </th> <th align="center">  $5p-5h$  </th> <th align="center">  $6p-6h$  </th> </tr>
</thead>
<tbody>
<tr><td align="center">   $0p-0h$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   0              </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   0              </td> <td align="center">   0              </td> <td align="center">   0              </td> <td align="center">   0              </td> </tr>
<tr><td align="center">   $1p-1h$    </td> <td align="center">   0              </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   0              </td> <td align="center">   0              </td> <td align="center">   0              </td> </tr>
<tr><td align="center">   $2p-2h$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   0              </td> <td align="center">   0              </td> </tr>
<tr><td align="center">   $3p-3h$    </td> <td align="center">   0              </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   0              </td> </tr>
<tr><td align="center">   $4p-4h$    </td> <td align="center">   0              </td> <td align="center">   0              </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> </tr>
<tr><td align="center">   $5p-5h$    </td> <td align="center">   0              </td> <td align="center">   0              </td> <td align="center">   0              </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> </tr>
<tr><td align="center">   $6p-6h$    </td> <td align="center">   0              </td> <td align="center">   0              </td> <td align="center">   0              </td> <td align="center">   0              </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> <td align="center">   $\tilde{x}$    </td> </tr>
</tbody>
</table>





## Shell-model jargon
If we do not make any truncations in the possible sets of Slater determinants (many-body states) we can make by distributing $A$ nucleons among $n$ single-particle states, we call such a calculation for **Full configuration interaction theory**

If we make truncations, we have different possibilities

* The standard nuclear shell-model. Here we define an effective Hilbert space with respect to a given core. The calculations are normally then performed for all many-body states that can be constructed from the effective Hilbert spaces. This approach requires a properly defined effective Hamiltonian

* We can truncate in the number of excitations. For example, we can limit the possible Slater determinants to only $1p-1h$ and $2p-2h$ excitations. This is called a configuration interaction calculation at the level of singles and doubles excitations, or just CISD. 

* We can limit the number of excitations in terms of the excitation energies. If we do not define a core, this defines normally what is called the no-core shell-model approach. 

What happens if we have a three-body interaction and a Hartree-Fock basis?




## FCI and the exponential growth
Full configuration interaction theory calculations provide in principle, if we can diagonalize numerically, all states of interest. The dimensionality of the problem explodes however quickly.

The total number of Slater determinants which can be built with say $N$ neutrons distributed among $n$ single particle states is

$$
\left (\begin{array}{c} n \\ N\end{array} \right) =\frac{n!}{(n-N)!N!}.
$$

For a model space which comprises the first for major shells only $0s$, $0p$, $1s0d$ and $1p0f$ we have $40$ single particle states for neutrons and protons.  For the eight neutrons of oxygen-16 we would then have

$$
\left (\begin{array}{c} 40 \\ 8\end{array} \right) =\frac{40!}{(32)!8!}\sim 10^{9},
$$

and multiplying this with the number of proton Slater determinants we end up with approximately with a dimensionality $d$ of $d\sim 10^{18}$.





## Exponential wall
This number can be reduced if we look at specific symmetries only. However, the dimensionality explodes quickly!

* For Hamiltonian matrices of dimensionalities  which are smaller than $d\sim 10^5$, we would use so-called direct methods for diagonalizing the Hamiltonian matrix

* For larger dimensionalities iterative eigenvalue solvers like Lanczos' method are used. The most efficient codes at present can handle matrices of $d\sim 10^{10}$.





## A non-practical way of solving the eigenvalue problem
To see this, we look at the contributions arising from

$$
\langle \Phi_H^P | = \langle \Phi_0|
$$

in  Eq. ([1](#eq:fullci)), that is we multiply with $\langle \Phi_0 |$
from the left in

$$
(\hat{H} -E)\sum_{P'H'}C_{H'}^{P'}|\Phi_{H'}^{P'} \rangle=0.
$$

If we assume that we have a two-body operator at most, Slater's rule gives then an equation for the 
correlation energy in terms of $C_i^a$ and $C_{ij}^{ab}$ only.  We get then

$$
\langle \Phi_0 | \hat{H} -E| \Phi_0\rangle + \sum_{ai}\langle \Phi_0 | \hat{H} -E|\Phi_{i}^{a} \rangle C_{i}^{a}+
\sum_{abij}\langle \Phi_0 | \hat{H} -E|\Phi_{ij}^{ab} \rangle C_{ij}^{ab}=0,
$$

or

$$
E-E_0 =\Delta E=\sum_{ai}\langle \Phi_0 | \hat{H}|\Phi_{i}^{a} \rangle C_{i}^{a}+
\sum_{abij}\langle \Phi_0 | \hat{H}|\Phi_{ij}^{ab} \rangle C_{ij}^{ab},
$$

where the energy $E_0$ is the reference energy and $\Delta E$ defines the so-called correlation energy.
The single-particle basis functions  could be the results of a Hartree-Fock calculation or just the eigenstates of the non-interacting part of the Hamiltonian.





## A non-practical way of solving the eigenvalue problem
To see this, we look at the contributions arising from

$$
\langle \Phi_H^P | = \langle \Phi_0|
$$

in  Eq. ([1](#eq:fullci)), that is we multiply with $\langle \Phi_0 |$
from the left in

$$
(\hat{H} -E)\sum_{P'H'}C_{H'}^{P'}|\Phi_{H'}^{P'} \rangle=0.
$$

## A non-practical way of solving the eigenvalue problem
If we assume that we have a two-body operator at most, Slater's rule gives then an equation for the 
correlation energy in terms of $C_i^a$ and $C_{ij}^{ab}$ only.  We get then

$$
\langle \Phi_0 | \hat{H} -E| \Phi_0\rangle + \sum_{ai}\langle \Phi_0 | \hat{H} -E|\Phi_{i}^{a} \rangle C_{i}^{a}+
\sum_{abij}\langle \Phi_0 | \hat{H} -E|\Phi_{ij}^{ab} \rangle C_{ij}^{ab}=0,
$$

or

$$
E-E_0 =\Delta E=\sum_{ai}\langle \Phi_0 | \hat{H}|\Phi_{i}^{a} \rangle C_{i}^{a}+
\sum_{abij}\langle \Phi_0 | \hat{H}|\Phi_{ij}^{ab} \rangle C_{ij}^{ab},
$$

where the energy $E_0$ is the reference energy and $\Delta E$ defines the so-called correlation energy.
The single-particle basis functions  could be the results of a Hartree-Fock calculation or just the eigenstates of the non-interacting part of the Hamiltonian.






## Rewriting the FCI equation
In our notes on Hartree-Fock calculations, 
we have already computed the matrix $\langle \Phi_0 | \hat{H}|\Phi_{i}^{a}\rangle $ and $\langle \Phi_0 | \hat{H}|\Phi_{ij}^{ab}\rangle$.  If we are using a Hartree-Fock basis, then the matrix elements
$\langle \Phi_0 | \hat{H}|\Phi_{i}^{a}\rangle=0$ and we are left with a *correlation energy* given by

$$
E-E_0 =\Delta E^{HF}=\sum_{abij}\langle \Phi_0 | \hat{H}|\Phi_{ij}^{ab} \rangle C_{ij}^{ab}.
$$

## Rewriting the FCI equation
Inserting the various matrix elements we can rewrite the previous equation as

$$
\Delta E=\sum_{ai}\langle i| \hat{f}|a \rangle C_{i}^{a}+
\sum_{abij}\langle ij | \hat{v}| ab \rangle C_{ij}^{ab}.
$$

This equation determines the correlation energy but not the coefficients $C$.




## Rewriting the FCI equation, does not stop here
We need more equations. Our next step is to set up

$$
\langle \Phi_i^a | \hat{H} -E| \Phi_0\rangle + \sum_{bj}\langle \Phi_i^a | \hat{H} -E|\Phi_{j}^{b} \rangle C_{j}^{b}+
\sum_{bcjk}\langle \Phi_i^a | \hat{H} -E|\Phi_{jk}^{bc} \rangle C_{jk}^{bc}+
\sum_{bcdjkl}\langle \Phi_i^a | \hat{H} -E|\Phi_{jkl}^{bcd} \rangle C_{jkl}^{bcd}=0,
$$

as this equation will allow us to find an expression for the coefficents $C_i^a$ since we can rewrite this equation as

$$
\langle i | \hat{f}| a\rangle +\langle \Phi_i^a | \hat{H}|\Phi_{i}^{a} \rangle C_{i}^{a}+ \sum_{bj\ne ai}\langle \Phi_i^a | \hat{H}|\Phi_{j}^{b} \rangle C_{j}^{b}+
\sum_{bcjk}\langle \Phi_i^a | \hat{H}|\Phi_{jk}^{bc} \rangle C_{jk}^{bc}+
\sum_{bcdjkl}\langle \Phi_i^a | \hat{H}|\Phi_{jkl}^{bcd} \rangle C_{jkl}^{bcd}=EC_i^a.
$$

## Rewriting the FCI equation, please stop here
We see that on the right-hand side we have the energy $E$. This leads to a non-linear equation in the unknown coefficients. 
These equations are normally solved iteratively ( that is we can start with a guess for the coefficients $C_i^a$). A common choice is to use perturbation theory for the first guess, setting thereby

$$
C_{i}^{a}=\frac{\langle i | \hat{f}| a\rangle}{\epsilon_i-\epsilon_a}.
$$

## Rewriting the FCI equation, more to add
The observant reader will however see that we need an equation for $C_{jk}^{bc}$ and $C_{jkl}^{bcd}$ as well.
To find equations for these coefficients we need then to continue our multiplications from the left with the various
$\Phi_{H}^P$ terms. 


For $C_{jk}^{bc}$ we need then

4
4
 
<
<
<
!
!
M
A
T
H
_
B
L
O
C
K

$$
\sum_{cdkl}\langle \Phi_{ij}^{ab} | \hat{H} -E|\Phi_{kl}^{cd} \rangle C_{kl}^{cd}+\sum_{cdeklm}\langle \Phi_{ij}^{ab} | \hat{H} -E|\Phi_{klm}^{cde} \rangle C_{klm}^{cde}+\sum_{cdefklmn}\langle \Phi_{ij}^{ab} | \hat{H} -E|\Phi_{klmn}^{cdef} \rangle C_{klmn}^{cdef}=0,
$$

and we can isolate the coefficients $C_{kl}^{cd}$ in a similar way as we did for the coefficients $C_{i}^{a}$.






## Rewriting the FCI equation, more to add
A standard choice for the first iteration is to set

$$
C_{ij}^{ab} =\frac{\langle ij \vert \hat{v} \vert ab \rangle}{\epsilon_i+\epsilon_j-\epsilon_a-\epsilon_b}.
$$

At the end we can rewrite our solution of the Schroedinger equation in terms of $n$ coupled equations for the coefficients $C_H^P$.
This is a very cumbersome way of solving the equation. However, by using this iterative scheme we can illustrate how we can compute the
various terms in the wave operator or correlation operator $\hat{C}$. We will later identify the calculation of the various terms $C_H^P$
as parts of different many-body approximations to full CI. In particular, we can  relate this non-linear scheme with Coupled Cluster theory and
many-body perturbation theory.





## Summarizing FCI and bringing in approximative methods

If we can diagonalize large matrices, FCI is the method of choice since:
* It gives all eigenvalues, ground state and excited states

* The eigenvectors are obtained directly from the coefficients $C_H^P$ which result from the diagonalization

* We can compute easily expectation values of other operators, as well as transition probabilities

* Correlations are easy to understand in terms of contributions to a given operator beyond the Hartree-Fock contribution. This is the standard approach in  many-body theory.




## Definition of the correlation energy
The correlation energy is defined as, with a two-body Hamiltonian,

$$
\Delta E=\sum_{ai}\langle i| \hat{f}|a \rangle C_{i}^{a}+
\sum_{abij}\langle ij | \hat{v}| ab \rangle C_{ij}^{ab}.
$$

The coefficients $C$ result from the solution of the eigenvalue problem. 
The energy of say the ground state is then

$$
E=E_{ref}+\Delta E,
$$

where the so-called reference energy is the energy we obtain from a Hartree-Fock calculation, that is

$$
E_{ref}=\langle \Phi_0 \vert \hat{H} \vert \Phi_0 \rangle.
$$

## FCI equation and the coefficients

However, as we have seen, even for a small case like the four first major shells and a nucleus like oxygen-16, the dimensionality becomes quickly intractable. If we wish to include single-particle states that reflect weakly bound systems, we need a much larger single-particle basis. We need thus approximative methods that sum specific correlations to infinite order. 

Popular methods are
* [Many-body perturbation theory (in essence a Taylor expansion)](http://www.sciencedirect.com/science/article/pii/0370157395000126)

* [Coupled cluster theory (coupled non-linear equations)](http://iopscience.iop.org/article/10.1088/0034-4885/77/9/096302/meta)

* Green's function approaches (matrix inversion)

* [Similarity group transformation methods (coupled ordinary differential equations)](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.106.222502)

All these methods start normally with a Hartree-Fock basis as the calculational basis.




## Important ingredients to have in codes

* Be able to validate and verify  the  algorithms. 

* Include concepts like unit testing. Gives the possibility to test and validate several or all parts of the code.

* Validation and verification are then included *naturally* and one can develop a better attitude to what is meant with an ethically sound scientific approach.






## A structured approach to solving problems
In the steps that lead to the development of clean code you should  think of 
1. How to structure a code in terms of functions  (use IDEs or advanced text editors like sublime or atom)

2. How to make a module

3. How to read input data flexibly from the command line or files

4. How to create graphical/web user interfaces

5. How to write unit tests  

6. How to refactor code in terms of classes (instead of functions only)

7. How to conduct and automate large-scale numerical experiments

8. How to write scientific reports in various formats (LaTeX, HTML, doconce)





## Additional benefits
Many of the above aspetcs  will save you a lot of time when you incrementally extend software over time from simpler to more complicated problems. In particular, you will benefit from many good habits:
1. New code is added in a modular fashion to a library (modules)

2. Programs are run through convenient user interfaces

3. It takes one quick command to let all your code undergo heavy testing 

4. Tedious manual work with running programs is automated,

5. Your scientific investigations are reproducible, scientific reports with top quality typesetting are produced both for paper and electronic devices. Use version control software like [git](https://git-scm.com/) and repositories like [github](https://github.com/)






## Unit Testing
Unit Testing is the practice of testing the smallest testable parts,
called units, of an application individually and independently to
determine if they behave exactly as expected. 

Unit tests (short code
fragments) are usually written such that they can be preformed at any
time during the development to continually verify the behavior of the
code. 

In this way, possible bugs will be identified early in the
development cycle, making the debugging at later stages much
easier.




## Unit Testing, benefits
There are many benefits associated with Unit Testing, such as
  * It increases confidence in changing and maintaining code. Big changes can be made to the code quickly, since the tests will ensure that everything still is working properly.

  * Since the code needs to be modular to make Unit Testing possible, the code will be easier to reuse. This improves the code design.

  * Debugging is easier, since when a test fails, only the latest changes need to be debugged.

   * Different parts of a project can be tested without the need to wait for the other parts to be available.


  * A unit test can serve as a documentation on the functionality of a unit of the code.





## Simple example of unit test
Look up the guide on how to install unit tests for c++ at course webpage. This is the version with classes.

        #include <unittest++/UnitTest++.h>
        
        class MyMultiplyClass{
        public:
            double multiply(double x, double y) {
                return x * y;
            }
        };
        
        TEST(MyMath) {
            MyMultiplyClass my;
            CHECK_EQUAL(56, my.multiply(7,8));
        }
        
        int main()
        {
            return UnitTest::RunAllTests();
        }


## Simple example of unit test
And without classes

        #include <unittest++/UnitTest++.h>
        
        
        double multiply(double x, double y) {
            return x * y;
        }
        
        TEST(MyMath) {
            CHECK_EQUAL(56, multiply(7,8));
        }
        
        int main()
        {
            return UnitTest::RunAllTests();
        } 


For Fortran users, the link at <http://sourceforge.net/projects/fortranxunit/> contains a similar
software for unit testing. For Python go to <https://docs.python.org/2/library/unittest.html>.








## [Unit tests](https://github.com/philsquared/Catch/blob/master/docs/tutorial.md)
There are many types of **unit test** libraries. One which is very popular with C++ programmers is [Catch](https://github.com/philsquared/Catch/blob/master/docs/tutorial.md)

Catch is header only. All you need to do is drop the file(s) somewhere reachable from your project - either in some central location you can set your header search path to find, or directly into your project tree itself! 

This is a particularly good option for other Open-Source projects that want to use Catch for their test suite.




## Examples

Computing factorials

        inline unsigned int Factorial( unsigned int number ) {
          return number > 1 ? Factorial(number-1)*number : 1;
        }


## Factorial Example

Simple test where we put everything in a single file

        #define CATCH_CONFIG_MAIN  // This tells Catch to provide a main()
        #include "catch.hpp"
        inline unsigned int Factorial( unsigned int number ) {
          return number > 1 ? Factorial(number-1)*number : 1;
        }
        
        TEST_CASE( "Factorials are computed", "[factorial]" ) {
            REQUIRE( Factorial(0) == 1 );
            REQUIRE( Factorial(1) == 1 );
            REQUIRE( Factorial(2) == 2 );
            REQUIRE( Factorial(3) == 6 );
            REQUIRE( Factorial(10) == 3628800 );
        }
        


This will compile to a complete executable which responds to command line arguments. If you just run it with no arguments it will execute all test cases (in this case there is just one), report any failures, report a summary of how many tests passed and failed and return the number of failed tests.


## What did we do (1)?
All we did was

        #define 


one identifier and

        #include 


one header and we got everything - even an implementation of main() that will respond to command line arguments. 
Once you have more than one file with unit tests in you'll just need to

        #include "catch.hpp" 


and go. Usually it's a good idea to have a dedicated implementation file that just has

        #define CATCH_CONFIG_MAIN 
        #include "catch.hpp". 


You can also provide your own implementation of main and drive Catch yourself.



## What did we do (2)?
We introduce test cases with the

        TEST_CASE 


macro.

The test name must be unique. You can run sets of tests by specifying a wildcarded test name or a tag expression. 
All we did was **define** one identifier and **include** one header and we got everything.

We write our individual test assertions using the

        REQUIRE 


macro.



## Unit test summary and testing approach
Three levels of tests
1. Microscopic level: testing small parts of code, use often unit test libraries

2. Mesoscopic level: testing the integration of various parts  of your code

3. Macroscopic level: testing that the final result is ok

 




## Coding Recommendations
Writing clean and clear code is an art and reflects 
your understanding of 

1. derivation, verification, and implementation of algorithms

2. what can go wrong with algorithms

3. overview of important, known algorithms

4. how algorithms are used to solve mathematical problems

5. reproducible science and ethics

6. algorithmic thinking for gaining deeper insights about scientific problems

Computing is understanding and your understanding is reflected in your abilities to
write clear and clean code.



## Summary and recommendations
Some simple hints and tips in order to write clean and clear code
1. Spell out the algorithm and have a top-down approach to the flow of data

2. Start with coding as close as possible to eventual mathematical expressions

3. Use meaningful names for variables

4. Split tasks in simple functions and modules/classes

5. Functions should return as few as possible variables

6. Use unit tests and make sure your codes are producing the correct results

7. Where possible use symbolic coding to autogenerate code and check results

8. Make a proper timing of your algorithms

9. Use version control and make your science reproducible

10. Use IDEs or smart editors with debugging and analysis tools.

11. Automatize your computations interfacing high-level and compiled languages like C++ and Fortran.

12. .....

## Building a many-body basis
Here we will discuss how we can set up a single-particle basis which we can use in the various parts of our projects, from the simple pairing model to infinite nuclear matter. We will use here the simple pairing model to illustrate in particular how to set up a single-particle basis. We will also use this do discuss standard FCI approaches like:
1. Standard shell-model basis in one or two major shells

2. Full CI in a given basis and no truncations

3. CISD and CISDT approximations

4. No-core shell model and truncation in excitation energy




## Building a many-body basis
An important step in an FCI code  is to construct the many-body basis.  

While the formalism is independent of the choice of basis, the **effectiveness** of a calculation 
will certainly be basis dependent. 

Furthermore there are common conventions useful to know.

First, the single-particle basis has angular momentum as a good quantum number.  You can 
imagine the single-particle wavefunctions being generated by a one-body Hamiltonian, 
for example a harmonic oscillator.  Modifications include harmonic oscillator plus 
spin-orbit splitting, or self-consistent mean-field potentials, or the Woods-Saxon potential which mocks 
up the self-consistent mean-field. 
For nuclei, the harmonic oscillator, modified by spin-orbit splitting, provides a useful language 
for describing single-particle states.




## Building a many-body basis
Each single-particle state is labeled by the following quantum numbers: 

* Orbital angular momentum $l$

* Intrinsic spin $s$ = 1/2 for protons and neutrons

* Angular momentum $j = l \pm 1/2$

* $z$-component $j_z$ (or $m$)

* Some labeling of the radial wavefunction, typically $n$ the number of nodes in  the radial wavefunction, but in the case of harmonic oscillator one can also use the principal quantum number $N$, where the harmonic oscillator energy is $(N+3/2)\hbar \omega$.  

In this format one labels states by $n(l)_j$, with $(l)$ replaced by a letter:
$s$ for $l=0$, $p$ for $l=1$, $d$ for $l=2$, $f$ for $l=3$, and thenceforth alphabetical.




## Building a many-body basis
 In practice the single-particle space has to be severely truncated.  This truncation is 
typically based upon the single-particle energies, which is the effective energy 
from a mean-field potential. 

Sometimes we freeze the core and only consider a valence space. For example, one 
may assume a frozen $^{4}\mbox{He}$ core, with two protons and two neutrons in the $0s_{1/2}$ 
shell, and then only allow active particles in the $0p_{1/2}$ and $0p_{3/2}$ orbits. 


Another example is a frozen $^{16}\mbox{O}$ core, with eight protons and eight neutrons filling the 
$0s_{1/2}$,  $0p_{1/2}$ and $0p_{3/2}$ orbits, with valence particles in the 
$0d_{5/2}, 1s_{1/2}$ and $0d_{3/2}$ orbits.


Sometimes we refer to nuclei by the valence space where their last nucleons go.  
So, for example, we call $^{12}\mbox{C}$ a $p$-shell nucleus, while $^{26}\mbox{Al}$ is an 
$sd$-shell nucleus and $^{56}\mbox{Fe}$ is a $pf$-shell nucleus.





## Building a many-body basis
There are different kinds of truncations.

* For example, one can start with `filled' orbits (almost always the lowest), and then  allow one, two, three... particles excited out of those filled orbits. These are called  1p-1h, 2p-2h, 3p-3h excitations. 

* Alternately, one can state a maximal orbit and allow all possible configurations with  particles occupying states up to that maximum. This is called *full configuration*.

* Finally, for particular use in nuclear physics, there is the *energy* truncation, also  called the $N\hbar\Omega$ or $N_{max}$ truncation.




## Building a many-body basis
Here one works in a harmonic oscillator basis, with each major oscillator shell assigned  a principal quantum number $N=0,1,2,3,...$. 
The $N\hbar\Omega$ or $N_{max}$ truncation: Any configuration is given an noninteracting energy, which is the sum 
of the single-particle harmonic oscillator energies. (Thus this ignores 
spin-orbit splitting.)

Excited state are labeled relative to the lowest configuration by the 
number of harmonic oscillator quanta.

This truncation is useful because if one includes *all* configuration up to 
some $N_{max}$, and has a translationally invariant interaction, then the intrinsic 
motion and the center-of-mass motion factor. In other words, we can know exactly 
the center-of-mass wavefunction. 

In almost all cases, the many-body Hamiltonian is rotationally invariant. This means 
it commutes with the operators $\hat{J}^2, \hat{J}_z$ and so eigenstates will have 
good $J,M$. Furthermore, the eigenenergies do not depend upon the orientation $M$. 


Therefore we can choose to construct a many-body basis which has fixed $M$; this is 
called an $M$-scheme basis. 


Alternately, one can construct a many-body basis which has fixed $J$, or a $J$-scheme 
basis.




## Building a many-body basis
The Hamiltonian matrix will have smaller dimensions (a factor of 10 or more) in the $J$-scheme than in the $M$-scheme. 
On the other hand, as we'll show in the next slide, the $M$-scheme is very easy to 
construct with Slater determinants, while the $J$-scheme basis states, and thus the 
matrix elements, are more complicated, almost always being linear combinations of 
$M$-scheme states. $J$-scheme bases are important and useful, but we'll focus on the 
simpler $M$-scheme.

The quantum number $m$ is additive (because the underlying group is Abelian): 
if a Slater determinant $\hat{a}_i^\dagger \hat{a}^\dagger_j \hat{a}^\dagger_k \ldots | 0 \rangle$ 
is built from single-particle states all with good $m$, then the total

$$
M = m_i + m_j + m_k + \ldots
$$

This is *not* true of $J$, because the angular momentum group SU(2) is not Abelian.





## Building a many-body basis

The upshot is that 
* It is easy to construct a Slater determinant with good total $M$;

* It is trivial to calculate $M$ for each Slater determinant;

* So it is easy to construct an $M$-scheme basis with fixed total $M$.

Note that the individual $M$-scheme basis states will *not*, in general, 
have good total $J$. 
Because the Hamiltonian is rotationally invariant, however, the eigenstates will 
have good $J$. (The situation is muddied when one has states of different $J$ that are 
nonetheless degenerate.)







## Building a many-body basis
Example: two $j=1/2$ orbits

<table border="1">
<thead>
<tr><th align="center">Index</th> <th align="center">$n$</th> <th align="center">$l$</th> <th align="center">$j$</th> <th align="center">$m_j$</th> </tr>
</thead>
<tbody>
<tr><td align="center">   1        </td> <td align="center">   0      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   2        </td> <td align="center">   0      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
<tr><td align="center">   3        </td> <td align="center">   1      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   4        </td> <td align="center">   1      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
</tbody>
</table>
Note that the order is arbitrary.




## Building a many-body basis
There are $\left ( \begin{array}{c} 4 \\ 2 \end{array} \right) = 6$ two-particle states, 
which we list with the total $M$:

<table border="1">
<thead>
<tr><th align="center">Occupied</th> <th align="center">$M$</th> </tr>
</thead>
<tbody>
<tr><td align="center">   1,2         </td> <td align="center">   0      </td> </tr>
<tr><td align="center">   1,3         </td> <td align="center">   -1     </td> </tr>
<tr><td align="center">   1,4         </td> <td align="center">   0      </td> </tr>
<tr><td align="center">   2,3         </td> <td align="center">   0      </td> </tr>
<tr><td align="center">   2,4         </td> <td align="center">   1      </td> </tr>
<tr><td align="center">   3,4         </td> <td align="center">   0      </td> </tr>
</tbody>
</table>
There are 4 states with $M= 0$, 
and 1 each with $M = \pm 1$.





## Building a many-body basis
As another example, consider using only single particle states from the $0d_{5/2}$ space. 
They have the following quantum numbers

<table border="1">
<thead>
<tr><th align="center">Index</th> <th align="center">$n$</th> <th align="center">$l$</th> <th align="center">$j$</th> <th align="center">$m_j$</th> </tr>
</thead>
<tbody>
<tr><td align="center">   1        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   -5/2     </td> </tr>
<tr><td align="center">   2        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   -3/2     </td> </tr>
<tr><td align="center">   3        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   4        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   1/2      </td> </tr>
<tr><td align="center">   5        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   3/2      </td> </tr>
<tr><td align="center">   6        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   5/2      </td> </tr>
</tbody>
</table>




## Building a many-body basis
There are $\left ( \begin{array}{c} 6 \\ 2 \end{array} \right) = 15$ two-particle states, 
which we list with the total $M$:

<table border="1">
<thead>
<tr><th align="center">Occupied</th> <th align="center">$M$</th> <th align="center">Occupied</th> <th align="center">$M$</th> <th align="center">Occupied</th> <th align="center">$M$</th> </tr>
</thead>
<tbody>
<tr><td align="center">   1,2         </td> <td align="center">   -4     </td> <td align="center">   2,3         </td> <td align="center">   -2     </td> <td align="center">   3,5         </td> <td align="center">   1      </td> </tr>
<tr><td align="center">   1,3         </td> <td align="center">   -3     </td> <td align="center">   2,4         </td> <td align="center">   -1     </td> <td align="center">   3,6         </td> <td align="center">   2      </td> </tr>
<tr><td align="center">   1,4         </td> <td align="center">   -2     </td> <td align="center">   2,5         </td> <td align="center">   0      </td> <td align="center">   4,5         </td> <td align="center">   2      </td> </tr>
<tr><td align="center">   1,5         </td> <td align="center">   -1     </td> <td align="center">   2,6         </td> <td align="center">   1      </td> <td align="center">   4,6         </td> <td align="center">   3      </td> </tr>
<tr><td align="center">   1,6         </td> <td align="center">   0      </td> <td align="center">   3,4         </td> <td align="center">   0      </td> <td align="center">   5,6         </td> <td align="center">   4      </td> </tr>
</tbody>
</table>
There are 3 states with $M= 0$, 2 with $M = 1$, and so on.













## Shell-model project

The first step  is to construct the $M$-scheme basis of Slater determinants.
Here $M$-scheme means the total $J_z$ of the many-body states is fixed.

The steps could be:

* Read in a user-supplied file of single-particle states (examples can be given) or just code these internally;

* Ask for the total $M$ of the system and the number of particles $N$;

* Construct all the $N$-particle states with given $M$.  You will validate the code by  comparing both the number of states and specific states.




## Shell-model project
The format of a possible input  file could be
<table border="1">
<thead>
<tr><th align="center">Index</th> <th align="center">$n$</th> <th align="center">$l$</th> <th align="center">$2j$</th> <th align="center">$2m_j$</th> </tr>
</thead>
<tbody>
<tr><td align="center">   1        </td> <td align="center">   1      </td> <td align="center">   0      </td> <td align="center">   1       </td> <td align="center">   -1        </td> </tr>
<tr><td align="center">   2        </td> <td align="center">   1      </td> <td align="center">   0      </td> <td align="center">   1       </td> <td align="center">   1         </td> </tr>
<tr><td align="center">   3        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   3       </td> <td align="center">   -3        </td> </tr>
<tr><td align="center">   4        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   3       </td> <td align="center">   -1        </td> </tr>
<tr><td align="center">   5        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   3       </td> <td align="center">   1         </td> </tr>
<tr><td align="center">   6        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   3       </td> <td align="center">   3         </td> </tr>
<tr><td align="center">   7        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5       </td> <td align="center">   -5        </td> </tr>
<tr><td align="center">   8        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5       </td> <td align="center">   -3        </td> </tr>
<tr><td align="center">   9        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5       </td> <td align="center">   -1        </td> </tr>
<tr><td align="center">   10       </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5       </td> <td align="center">   1         </td> </tr>
<tr><td align="center">   11       </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5       </td> <td align="center">   3         </td> </tr>
<tr><td align="center">   12       </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5       </td> <td align="center">   5         </td> </tr>
</tbody>
</table>
This represents the $1s_{1/2}0d_{3/2}0d_{5/2}$ valence space, or just the $sd$-space.  There are 
twelve single-particle states, labeled by an overall index, and which have associated quantum 
numbers the number of radial nodes, the orbital angular momentum $l$, and the 
angular momentum $j$ and third component $j_z$.  To keep everything as integers, we could store $2 \times j$ and 
$2 \times j_z$.




## Shell-model project
To read in the single-particle states you need to:
* Open the file 

 * Read the number of single-particle states (in the above example, 12);  allocate memory; all you need is a single array storing $2\times j_z$ for each state, labeled by the index.


* Read in the quantum numbers and store $2 \times j_z$ (and anything else you happen to want).




## Shell-model project

The next step is to read in the number of particles $N$ and the fixed total $M$ (or, actually, $2 \times M$). 
For this project we assume only a single species of particles, say neutrons, although this can be 
relaxed. **Note**: Although it is often a good idea to try to write a more general code, given the 
short time alloted we would suggest you keep your ambition in check, at least in the initial phases of the 
project.  


You should probably write an error trap to make sure $N$ and $M$ are congruent; if $N$ is even, then 
$2 \times M$ should be even, and if $N$ is odd then $2\times M$ should be odd.




## Shell-model project
The final step is to generate the set of $N$-particle Slater determinants with fixed $M$. 
The Slater determinants will be stored in occupation representation.  Although in many codes
this representation is done compactly in bit notation with ones and zeros, but for 
greater transparency and simplicity we will list the occupied single particle states.

 Hence we can 
store the Slater determinant basis states as $sd(i,j)$, that is an 
array of dimension $N_{SD}$, the number of Slater determinants, by $N$, the number of occupied 
state. So if for the 7th Slater determinant the 2nd, 3rd, and 9th single-particle states are occupied, 
then $sd(7,1) = 2$, $sd(7,2) = 3$, and $sd(7,3) = 9$.




## Shell-model project

We can construct an occupation representation of Slater determinants by the *odometer*
method.  Consider $N_{sp} = 12$ and $N=4$. 
Start with the first 4 states occupied, that is:

* $sd(1,:)= 1,2,3,4$ (also written as $|1,2,3,4 \rangle$)

Now increase the last occupancy recursively:
* $sd(2,:)= 1,2,3,5$

* $sd(3,:)= 1,2,3,6$

* $sd(4,:)= 1,2,3,7$

* $\ldots$

* $sd(9,:)= 1,2,3,12$

Then start over with 
* $sd(10,:)= 1,2,4,5$

and again increase the rightmost digit

* $sd(11,:)= 1,2,4,6$

* $sd(12,:)= 1,2,4,7$

* $\ldots$

* $sd(17,:)= 1,2,4,12$




## Shell-model project
When we restrict ourselves to an $M$-scheme basis, we could choose two paths. 
The first is simplest (and simplest is often best, at 
least in the first draft of a code): generate all possible Slater determinants, 
and then extract from this initial list a list of those Slater determinants with a given 
$M$. (You will need to write a short function or routine that computes $M$ for any 
given occupation.)  


Alternately, and not too difficult, is to run the odometer routine twice: each time, as 
as a Slater determinant is calculated, compute $M$, but do not store the Slater determinants 
except the current one. You can then count up the number of Slater determinants with a 
chosen $M$.  Then allocated storage for the Slater determinants, and run the odometer 
algorithm again, this time storing Slater determinants with the desired $M$ (this can be 
done with a simple logical flag).





## Shell-model project

*Some example solutions*:  Let's begin with a simple case, the $0d_{5/2}$ space containing six single-particle states

<table border="1">
<thead>
<tr><th align="center">Index</th> <th align="center">$n$</th> <th align="center">$l$</th> <th align="center">$j$</th> <th align="center">$m_j$</th> </tr>
</thead>
<tbody>
<tr><td align="center">   1        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   -5/2     </td> </tr>
<tr><td align="center">   2        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   -3/2     </td> </tr>
<tr><td align="center">   3        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   4        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   1/2      </td> </tr>
<tr><td align="center">   5        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   3/2      </td> </tr>
<tr><td align="center">   6        </td> <td align="center">   0      </td> <td align="center">   2      </td> <td align="center">   5/2    </td> <td align="center">   5/2      </td> </tr>
</tbody>
</table>
For two particles, there are a total of 15 states, which we list here with the total $M$:
* $\vert 1,2 \rangle$, $M= -4$,  $\vert 1,3 \rangle$, $M= -3$

* $\vert  1,4 \rangle$, $M= -2$, $\vert 1,5 \rangle$, $M= -1$

* $\vert 1,5 \rangle$, $M= 0$, $vert 2,3 \rangle$, $M= -2$

* $\vert 2,4 \rangle$, $M= -1$, $\vert 2,5 \rangle$, $M= 0$

* $\vert 2,6 \rangle$, $M= 1$, $\vert 3,4 \rangle$, $M= 0$

* $\vert 3,5 \rangle$, $M= 1$, $\vert 3,6 \rangle$, $M= 2$

* $\vert 4,5 \rangle$, $M= 2$, $\vert 4,6 \rangle$, $M= 3$

* $\vert 5,6 \rangle$, $M= 4$

Of these, there are only 3 states with $M=0$.




## Shell-model project
*You should try* by hand to show that in this same single-particle space, that for 
$N=3$ there are 3 states with $M=1/2$ and for $N= 4$ there are also only 3 states with $M=0$. 

*To test your code*, confirm the above. 

Also, 
for the $sd$-space given above, for $N=2$ there are 14 states with $M=0$, for $N=3$ there are 37 
states with $M=1/2$, for $N=4$ there are 81 states with $M=0$.




## Shell-model project
For our project, we will only consider the pairing model.
A simple space is the $(1/2)^2$ space with four single-particle states

<table border="1">
<thead>
<tr><th align="center">Index</th> <th align="center">$n$</th> <th align="center">$l$</th> <th align="center">$s$</th> <th align="center">$m_s$</th> </tr>
</thead>
<tbody>
<tr><td align="center">   1        </td> <td align="center">   0      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   2        </td> <td align="center">   0      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
<tr><td align="center">   3        </td> <td align="center">   1      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   4        </td> <td align="center">   1      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
</tbody>
</table>
For $N=2$ there are 4 states with $M=0$; show this by hand and confirm your code reproduces it.




## Shell-model project
Another, slightly more challenging space is the $(1/2)^4$ space, that is, 
with eight  single-particle states we have

<table border="1">
<thead>
<tr><th align="center">Index</th> <th align="center">$n$</th> <th align="center">$l$</th> <th align="center">$s$</th> <th align="center">$m_s$</th> </tr>
</thead>
<tbody>
<tr><td align="center">   1        </td> <td align="center">   0      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   2        </td> <td align="center">   0      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
<tr><td align="center">   3        </td> <td align="center">   1      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   4        </td> <td align="center">   1      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
<tr><td align="center">   5        </td> <td align="center">   2      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   6        </td> <td align="center">   2      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
<tr><td align="center">   7        </td> <td align="center">   3      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   8        </td> <td align="center">   3      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
</tbody>
</table>
For $N=2$ there are 16 states with $M=0$; for $N=3$ there are 24 states with $M=1/2$, and for 
$N=4$ there are 36 states with $M=0$.




## Shell-model project
In the shell-model context we can interpret this as 4 $s_{1/2}$ levels, with $m = \pm 1/2$, we can also think of these are simple four pairs,  $\pm k, k = 1,2,3,4$. Later on we will 
assign single-particle energies,  depending on the radial quantum number $n$, that is, 
$\epsilon_k = |k| \delta$ so that they are equally spaced.




## Shell-model project

For application in the pairing model we can go further and consider only states with 
no "broken pairs," that is, if $+k$ is filled (or $m = +1/2$, so is $-k$ ($m=-1/2$). 
If you want, you can write your code to accept only these, and obtain the following 
six states:

* $|           1,           2 ,          3         ,       4  \rangle , $

* $|            1      ,     2        ,        5         ,       6 \rangle , $

* $|            1         ,       2     ,           7         ,       8  \rangle , $

* $|            3        ,        4      ,          5          ,      6  \rangle , $

* $|            3        ,        4      ,          7         ,       8  \rangle , $

* $|            5        ,        6     ,           7     ,           8  \rangle $






## Shell-model project
**Hints for coding.**



* Write small modules (routines/functions) ; avoid big functions  that do everything. (But not too small.)

* Use Unit tests! Write lots of error traps, even for things that are `obvious.'

* Document as you go along. The Unit tests serve as documentation. For each function write a header that includes: 

a. Main purpose of function and/or unit test

b. names and  brief explanation of input variables, if any 

c. names and brief explanation of output variables, if any

d. functions called by this function

e. called by which functions




## Shell-model project

Hints for coding

* Unit tests will save time. Use also IDEs for debugging. If you insist on brute force debugging, print out intermediate values. It's almost impossible to debug a  code by looking at it - the code will almost always win a `staring contest.'

* Validate code with SIMPLE CASES. Validate early and often.  Unit tests!! 

The number one mistake is using a too complex a system to test. For example ,
if you are computing particles in a potential in a box, try removing the potential - you should get 
particles in a box. And start with one particle, then two, then three... Don't start with 
eight particles.




## Shell-model project

Our recommended occupation representation, e.g. $| 1,2,4,8 \rangle$, is 
easy to code, but numerically inefficient when one has hundreds of 
millions of Slater determinants.


In state-of-the-art shell-model codes, one generally uses bit 
representation, i.e. $|1101000100... \rangle$ where one stores 
the Slater determinant as a single (or a small number of) integer.


This is much more compact, but more intricate to code with considerable 
more overhead. There exist 
bit-manipulation functions. We will discuss these in more detail at the beginning of the third week.




## Example case: pairing Hamiltonian

We consider a space with $2\Omega$ single-particle states, with each 
state labeled by 
$k = 1, 2, 3, \Omega$ and $m = \pm 1/2$. The convention is that 
the state with $k>0$ has $m = + 1/2$ while $-k$ has $m = -1/2$.


The Hamiltonian we consider is

$$
\hat{H} = -G \hat{P}_+ \hat{P}_-,
$$

where

$$
\hat{P}_+ = \sum_{k > 0} \hat{a}^\dagger_k \hat{a}^\dagger_{-{k}}.
$$

and $\hat{P}_- = ( \hat{P}_+)^\dagger$.

This problem can be solved using what is called the quasi-spin formalism to obtain the 
exact results. Thereafter we will try again using the explicit Slater determinant formalism.






## Example case: pairing Hamiltonian

One can show (and this is part of the project) that

$$
\left [ \hat{P}_+, \hat{P}_- \right ] = \sum_{k> 0} \left( \hat{a}^\dagger_k \hat{a}_k 
+ \hat{a}^\dagger_{-{k}} \hat{a}_{-{k}} - 1 \right) = \hat{N} - \Omega.
$$

Now define

$$
\hat{P}_z = \frac{1}{2} ( \hat{N} -\Omega).
$$

Finally you can show

$$
\left [ \hat{P}_z , \hat{P}_\pm \right ] = \pm \hat{P}_\pm.
$$

This means the operators $\hat{P}_\pm, \hat{P}_z$ form a so-called  $SU(2)$ algebra, and we can 
use all our insights about angular momentum, even though there is no actual 
angular momentum involved.

So we rewrite the Hamiltonian to make this explicit:

$$
\hat{H} = -G \hat{P}_+ \hat{P}_- 
= -G \left( \hat{P}^2 - \hat{P}_z^2 + \hat{P}_z\right)
$$

## Example case: pairing Hamiltonian

Because of the SU(2) algebra, we know that the eigenvalues of 
$\hat{P}^2$ must be of the form $p(p+1)$, with $p$ either integer or half-integer, and the eigenvalues of $\hat{P}_z$ 
are $m_p$ with $p \geq | m_p|$, with $m_p$ also integer or half-integer. 


But because $\hat{P}_z = (1/2)(\hat{N}-\Omega)$, we know that for $N$ particles 
the value $m_p = (N-\Omega)/2$. Furthermore, the values of $m_p$ range from 
$-\Omega/2$ (for $N=0$) to $+\Omega/2$ (for $N=2\Omega$, with all states filled). 

We deduce the maximal $p = \Omega/2$ and for a given $n$ the 
values range of $p$ range from $|N-\Omega|/2$ to $\Omega/2$ in steps of 1 
(for an even number of particles) 


Following Racah we introduce the notation
$p = (\Omega - v)/2$
where $v = 0, 2, 4,..., \Omega - |N-\Omega|$ 
With this it is easy to deduce that the eigenvalues of the pairing Hamiltonian are

$$
-G(N-v)(2\Omega +2-N-v)/4
$$

This also works for $N$ odd, with $v= 1,3,5, \dots$.





## Example case: pairing Hamiltonian

Let's take a specific example: $\Omega = 3$ so there are 6 single-particle states, 
and $N = 3$, with $v= 1,3$. Therefore there are two distinct eigenvalues,

$$
E = -2G, 0
$$

Now let's work this out explicitly. The single particle degrees of freedom are defined as

<table border="1">
<thead>
<tr><th align="center">Index</th> <th align="center">$k$</th> <th align="center">$m$ </th> </tr>
</thead>
<tbody>
<tr><td align="center">   1        </td> <td align="center">   1      </td> <td align="center">   -1/2    </td> </tr>
<tr><td align="center">   2        </td> <td align="center">   -1     </td> <td align="center">   1/2     </td> </tr>
<tr><td align="center">   3        </td> <td align="center">   2      </td> <td align="center">   -1/2    </td> </tr>
<tr><td align="center">   4        </td> <td align="center">   -2     </td> <td align="center">   1/2     </td> </tr>
<tr><td align="center">   5        </td> <td align="center">   3      </td> <td align="center">   -1/2    </td> </tr>
<tr><td align="center">   6        </td> <td align="center">   -3     </td> <td align="center">   1/2     </td> </tr>
</tbody>
</table>
 There are  $\left( \begin{array}{c}6 \\ 3 \end{array} \right) = 20$ three-particle states, but there 
are 9 states with $M = +1/2$, namely
$| 1,2,3 \rangle, |1,2,5\rangle, | 1,4,6 \rangle, | 2,3,4 \rangle, |2,3,6 \rangle, | 2,4,5 \rangle, | 2, 5, 6 \rangle, |3,4,6 \rangle, | 4,5,6 \rangle$.








## Example case: pairing Hamiltonian

In this basis, the operator

$$
\hat{P}_+
= \hat{a}^\dagger_1 \hat{a}^\dagger_2 + \hat{a}^\dagger_3 \hat{a}^\dagger_4 +
\hat{a}^\dagger_5 \hat{a}^\dagger_6
$$

From this we can determine that

$$
\hat{P}_- | 1, 4, 6 \rangle = \hat{P}_- | 2, 3, 6 \rangle
= \hat{P}_- | 2, 4, 5 \rangle = 0
$$

so those states all have eigenvalue 0.





## Example case: pairing Hamiltonian
Now for further example,

$$
\hat{P}_- | 1,2,3 \rangle = | 3 \rangle
$$

so

$$
\hat{P}_+ \hat{P}_- | 1,2,3\rangle = | 1,2,3\rangle+ | 3,4,3\rangle + | 5,6,3\rangle
$$

The second term vanishes because state 3 is occupied twice, and reordering the last 
term we
get

$$
\hat{P}_+ \hat{P}_- | 1,2,3\rangle = | 1,2,3\rangle+ |3, 5,6\rangle
$$

without picking up a phase.




## Example case: pairing Hamiltonian

Continuing in this fashion, with the previous ordering of the many-body states
(  $| 1,2,3 \rangle, |1,2,5\rangle, | 1,4,6 \rangle, | 2,3,4 \rangle, |2,3,6 \rangle, | 2,4,5 \rangle, | 2, 5, 6 \rangle, |3,4,6 \rangle, | 4,5,6 \rangle$) the 
Hamiltonian matrix of this system is

$$
H = -G\left( 
\begin{array}{ccccccccc}
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1  \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0  \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0  \\
0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0  \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0  \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0  \\
0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0  \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0  \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0  \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1  
\end{array} \right )
$$

This is useful for our project.  One can by hand confirm 
that there are 3 eigenvalues $-2G$ and 6 with value zero.




## Example case: pairing Hamiltonian

Another example
Using the $(1/2)^4$ single-particle space, resulting in eight single-particle states

<table border="1">
<thead>
<tr><th align="center">Index</th> <th align="center">$n$</th> <th align="center">$l$</th> <th align="center">$s$</th> <th align="center">$m_s$</th> </tr>
</thead>
<tbody>
<tr><td align="center">   1        </td> <td align="center">   0      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   2        </td> <td align="center">   0      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
<tr><td align="center">   3        </td> <td align="center">   1      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   4        </td> <td align="center">   1      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
<tr><td align="center">   5        </td> <td align="center">   2      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   6        </td> <td align="center">   2      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
<tr><td align="center">   7        </td> <td align="center">   3      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   -1/2     </td> </tr>
<tr><td align="center">   8        </td> <td align="center">   3      </td> <td align="center">   0      </td> <td align="center">   1/2    </td> <td align="center">   1/2      </td> </tr>
</tbody>
</table>
and then taking only 4-particle, $M=0$ states that have no `broken pairs', there are six basis Slater 
determinants:

* $|           1,           2 ,          3         ,       4  \rangle , $

* $|            1      ,     2        ,        5         ,       6 \rangle , $

* $|            1         ,       2     ,           7         ,       8  \rangle , $

* $|            3        ,        4      ,          5          ,      6  \rangle , $

* $|            3        ,        4      ,          7         ,       8  \rangle , $

* $|            5        ,        6     ,           7     ,           8  \rangle $




## Example case: pairing Hamiltonian

Now we take the following Hamiltonian

$$
\hat{H} = \sum_n n \delta \hat{N}_n  - G \hat{P}^\dagger \hat{P}
$$

where

$$
\hat{N}_n = \hat{a}^\dagger_{n, m=+1/2} \hat{a}_{n, m=+1/2} +
\hat{a}^\dagger_{n, m=-1/2} \hat{a}_{n, m=-1/2}
$$

and

$$
\hat{P}^\dagger = \sum_{n} \hat{a}^\dagger_{n, m=+1/2} \hat{a}^\dagger_{n, m=-1/2}
$$

We can write down the $ 6 \times 6$  Hamiltonian in the basis from the prior slide:

$$
H = \left ( 
\begin{array}{cccccc}
2\delta -2G & -G & -G & -G & -G & 0 \\
 -G & 4\delta -2G & -G & -G & -0 & -G \\
-G & -G & 6\delta -2G & 0 & -G & -G \\
 -G & -G & 0 & 6\delta-2G & -G & -G \\
 -G & 0 & -G & -G & 8\delta-2G & -G \\
0 & -G & -G & -G & -G & 10\delta -2G 
\end{array} \right )
$$

(You should check by hand that this is correct.) 

For $\delta = 0$ we have the closed form solution of  the g.s. energy given by $-6G$.





## Building a Hamiltonian matrix
The goal is to compute the matrix elements of the Hamiltonian, specifically
matrix elements between many-body states (Slater determinants) of two-body
operators

$$
\sum_{p < q, r < s}V_{pqr} \hat{a}^\dagger_p \hat{a}^\dagger_q\hat{a}_s \hat{a}_r
$$

In particular we will need to compute

$$
\langle \beta | \hat{a}^\dagger_p \hat{a}^\dagger_q\hat{a}_s \hat{a}_r |\alpha \rangle
$$

where $\alpha, \beta$ are indices labeling Slater determinants and $p,q,r,s$ label
single-particle states.





## Building a Hamiltonian matrix
Note: there are other, more efficient ways to do this than the method we describe, 
but you will
be able to produce a working code quickly.

As we coded in the first step,
a Slater determinant $| \alpha \rangle$ with index $\alpha$ is a
list of $N$ occupied single-particle states $i_1 < i_2 < i_3 \ldots i_N$.


Furthermore, for the two-body matrix elements $V_{pqrs}$ we normally assume
$p < q$ and $r < s$. For our specific project, the interaction is much simpler and you can use this to simplify considerably the setup of a shell-model code for project 2.

What follows here is a more general, but still brute force, approach.





## Building a Hamiltonian matrix
Write a function that:
1. Has as input the single-particle indices $p,q,r,s$ for the two-body operator and the index $\alpha$ for the ket Slater determinant;

2. Returns the index $\beta$ of the unique (if any) Slater determinant such that

$$
| \beta \rangle = \pm \hat{a}^\dagger_p \hat{a}^\dagger_q\hat{a}_s \hat{a}_r |\alpha \rangle
$$

as well as the phase

This is equivalent to computing

$$
\langle \beta | \hat{a}^\dagger_p \hat{a}^\dagger_q\hat{a}_s \hat{a}_r |\alpha \rangle
$$

## Building a Hamiltonian matrix, first step
The first step can take as input an initial Slater determinant
(whose position in the list of basis Slater determinants is $\alpha$) written as an
ordered listed of occupied single-particle states, e.g. $1,2,5,8$, and the
indices $p,q,r,s$ from the two-body operator. 

It will return another final Slater determinant if the single-particle states $r$ and $s$ are occupied, else it will return an 
empty Slater determinant
(all zeroes). 

If $r$ and $s$ are in the list of occupied single particle states, then
replace the initial single-particle states $ij$ as $i \rightarrow r$ and $j \rightarrow r$.





## Building a Hamiltonian matrix, second step
The second step will take the final Slater determinant 
from the first step (if not empty),
and then order by pairwise permutations (i.e., if the Slater determinant is
$i_1, i_2, i_3, \ldots$, then if $i_n > i_{n+1}$, interchange 
$i_n \leftrightarrow i_{n+1}$.






## Building a Hamiltonian matrix

It will also output a phase.  If any two single-particle occupancies are repeated, 
the phase is
0.  Otherwise it is +1 for an even permutation and -1 for an odd permutation to 
bring the final
Slater determinant into ascending order, $j_1 < j_2 < j_3 \ldots$.





## Building a Hamiltonian matrix
**Example**: Suppose in the $sd$ single-particle space that the initial 
Slater determinant
is $1,3,9,12$. If $p,q,r,s = 2,8,1,12$, then after the first step the final Slater determinant
is $2,3,9,8$.  The second step will return $2,3,8,9$ and a phase of -1, 
because an odd number  of interchanges is required.





## Building a Hamiltonian matrix

**Example**: Suppose in the $sd$ single-particle space that the initial 
Slater determinant
is $1,3,9,12$. If $p,q,r,s = 3,8,1,12$, then after the first step the 
final  Slater determinant
is $3,3,9,8$, but after the second step the phase is 0 
because the single-particle state 3 is
occupied twice.

Lastly, the final step  takes the ordered final Slater determinant and 
we search through the basis list to
determine its index in the many-body basis, that is, $\beta$.





## Building a Hamiltonian matrix

The Hamiltonian is then stored as an $N_{SD} \times N_{SD}$ array of real numbers, which
can be allocated once you have created the many-body basis and know $N_{SD}$.





## Building a Hamiltonian matrix

1. Initialize $H(\alpha,\beta)=0.0$

2. Set up an outer loop over $\beta$

3. Loop over $\alpha = 1, NSD$

4. For each $\alpha$, loop over $a=1,ntbme$  and fetch $V(a)$ and the single-particle indices $p,q,r,s$ 

5. If $V(a) = 0$ skip.  Otherwise, apply $\hat{a}^\dagger_p\hat{a}^\dagger_q \hat{a}_s \hat{a}_r$ to the Slater determinant labeled by $\alpha$.

6. Find, if any, the label $\beta$ of the resulting Slater determinant and the phase (which is 0, +1, -1).

7. If phase $\neq 0$, then update $H(\alpha,\beta)$  as $H(\alpha,\beta) + phase*V(a)$. The sum is important because multiple operators might contribute to the same matrix element.

8. Continue loop over $a$

9. Continue loop over $\alpha$.

10. End the outer loop over $\beta$.

You should force the resulting matrix $H$ to be symmetric. To do this, when
updating $H(\alpha,\beta)$, if $\alpha \neq \beta$, also update $H(\beta,\alpha)$.





## Building a Hamiltonian matrix

You will also need to include the single-particle energies. This is easy: they only
contribute to diagonal matrix elements, that is, $H(\alpha,\alpha)$.  
Simply find the occupied single-particle states $i$ and add the corresponding $\epsilon(i)$.





## Hamiltonian matrix without the bit representation

Consider the many-body state $\Psi_{\lambda}$ expressed as linear combinations of
Slater determinants ($SD$) of orthonormal single-particle states $\phi({\bf r})$:

<!-- Equation labels as ordinary links -->
<div id="_auto1"></div>

$$
\begin{equation}
\Psi_{\lambda} = \sum_i C_{\lambda i} SD_i
\label{_auto1} \tag{2}
\end{equation}
$$

Using the Slater-Condon rules the matrix elements of any one-body
($\cal{O}_1$) or two-body ($\cal{O}_2$) operator expressed in the
determinant space have simple expressions involving one- and two-fermion
integrals in our given single-particle basis.
The diagonal elements are given by:

$$
\begin{eqnarray}
  \langle SD | \cal{O}_1 | SD \rangle & = & \sum_{i \in SD} \langle \phi_i | \cal{O}_1 | \phi_i \rangle \\
  \langle SD | \cal{O}_2 | SD \rangle & = & \frac{1}{2} \sum_{(i,j) \in SD}  
      \langle \phi_i \phi_j | \cal{O}_2 | \phi_i \phi_j \rangle - \nonumber \\
 & & 
      \langle \phi_i \phi_j | \cal{O}_2 | \phi_j \phi_i \rangle \nonumber 
\end{eqnarray}
$$

## Hamiltonian matrix without the bit representation, one and two-body operators

For two determinants which differ only by the substitution of single-particle states $i$ with
a single-particle state $j$:

$$
\begin{eqnarray}
  \langle SD | \cal{O}_1 | SD_i^j \rangle & = & \langle \phi_i | \cal{O}_1 | \phi_j \rangle \\
  \langle SD | \cal{O}_2 | SD_i^j \rangle & = & \sum_{k \in SD} 
      \langle \phi_i \phi_k | \cal{O}_2 | \phi_j \phi_k \rangle - 
      \langle \phi_i \phi_k | \cal{O}_2 | \phi_k \phi_j \rangle \nonumber
\end{eqnarray}
$$

For two determinants which differ by two single-particle states

$$
\begin{eqnarray}
  \langle SD | \cal{O}_1 | SD_{ik}^{jl} \rangle & = & 0 \\
  \langle SD | \cal{O}_2 | SD_{ik}^{jl} \rangle & = & 
      \langle \phi_i \phi_k | \cal{O}_2 | \phi_j \phi_l \rangle -
      \langle \phi_i \phi_k | \cal{O}_2 | \phi_l \phi_j \rangle \nonumber 
\end{eqnarray}
$$

All other matrix elements involving determinants with more than two
substitutions are zero.




## Strategies for setting up an algorithm


An efficient implementation of these rules requires

* to find the number of single-particle state substitutions between two determinants

* to find which single-particle states are involved in the substitution

* to compute the phase factor if a reordering of the single-particle states has occured

We can solve this problem using our odometric approach or alternatively using a bit representation as discussed below and in more detail in 

* [Scemama and Gimer's article (Fortran codes)](https://github.com/scemama/slater_condon)

* [Simen Kvaal's article on how to build an FCI code (C++ code)](https://arxiv.org/abs/0810.2644)

We recommend in particular the article by Simen Kvaal. It contains nice general classes for creation and annihilation operators as well as the calculation of the phase (see below).





## Computing expectation values and transitions in the shell-model
When we diagonalize the Hamiltonian matrix, the eigenvectors are the coefficients $C_{\lambda i}$ used 
to express the many-body state $\Psi_{\lambda}$ in terms of  a linear combinations of
Slater determinants ($SD$) of orthonormal single-particle states $\phi({\bf r})$.

With these eigenvectors we can compute say the transition likelyhood of a one-body operator as

$$
\langle \Psi_{\lambda} \vert \cal{O}_1 \vert \Psi_{\sigma} \rangle  = 
\sum_{ij}C_{\lambda i}^*C_{\sigma j}  \langle SD_i | \cal{O}_1 | SD_j \rangle .
$$

Writing the one-body operator in second quantization as

$$
\cal{O}_1  = \sum_{pq} \langle p \vert \cal{o}_1 \vert q\rangle a_p^{\dagger} a_q,
$$

we have

$$
\langle \Psi_{\lambda} \vert \cal{O}_1 \vert \Psi_{\sigma} \rangle  = 
\sum_{pq}\langle p \vert \cal{o}_1 \vert q\rangle \sum_{ij}C_{\lambda i}^*C_{\sigma j}  \langle SD_i |a_p^{\dagger} a_q | SD_j \rangle .
$$

## Computing expectation values and transitions in the shell-model and spectroscopic factors
The terms we need to evalute then are just the elements

$$
\langle SD_i |a_p^{\dagger} a_q | SD_j \rangle,
$$

which can be rewritten in terms of spectroscopic factors by inserting a complete set of Slater determinats as

$$
\langle SD_i |a_p^{\dagger} a_q | SD_j \rangle = \sum_{l}\langle SD_i \vert a_p^{\dagger}\vert SD_l\rangle \langle SD_l \vert  a_q \vert SD_j \rangle,
$$

where $\langle SD_l\vert a_q(a_p^{\dagger})\vert SD_j\rangle$ are the spectroscopic factors. These can be easily evaluated in $m$-scheme. Using the Wigner-Eckart theorem we can transform these to a $J$-coupled scheme through so-called reduced matrix elements.







## Operators in second quantization
In the build-up of a shell-model or FCI code that is meant to tackle large dimensionalities
we need to deal with the action of the Hamiltonian $\hat{H}$ on a
Slater determinant represented in second quantization as

$$
|\alpha_1\dots \alpha_n\rangle = a_{\alpha_1}^{\dagger} a_{\alpha_2}^{\dagger} \dots a_{\alpha_n}^{\dagger} |0\rangle.
$$

The time consuming part stems from the action of the Hamiltonian
on the above determinant,

$$
\left(\sum_{\alpha\beta} \langle \alpha|t+u|\beta\rangle a_\alpha^{\dagger} a_\beta + \frac{1}{4} \sum_{\alpha\beta\gamma\delta}
                \langle \alpha \beta|\hat{v}|\gamma \delta\rangle a_\alpha^{\dagger} a_\beta^{\dagger} a_\delta a_\gamma\right)a_{\alpha_1}^{\dagger} a_{\alpha_2}^{\dagger} \dots a_{\alpha_n}^{\dagger} |0\rangle.
$$

A practically useful way to implement this action is to encode a Slater determinant as a bit pattern.





## Operators in second quantization
Assume that we have at our disposal $n$ different single-particle states
$\alpha_0,\alpha_2,\dots,\alpha_{n-1}$ and that we can distribute  among these states $N\le n$ particles.

A Slater  determinant can then be coded as an integer of $n$ bits. As an example, if we have $n=16$ single-particle states
$\alpha_0,\alpha_1,\dots,\alpha_{15}$ and $N=4$ fermions occupying the states $\alpha_3$, $\alpha_6$, $\alpha_{10}$ and $\alpha_{13}$
we could write this Slater determinant as

$$
\Phi_{\Lambda} = a_{\alpha_3}^{\dagger} a_{\alpha_6}^{\dagger} a_{\alpha_{10}}^{\dagger} a_{\alpha_{13}}^{\dagger} |0\rangle.
$$

The unoccupied single-particle states have bit value $0$ while the occupied ones are represented by bit state $1$. 
In the binary notation we would write this   16 bits long integer as

$$
\begin{array}{cccccccccccccccc}
{\alpha_0}&{\alpha_1}&{\alpha_2}&{\alpha_3}&{\alpha_4}&{\alpha_5}&{\alpha_6}&{\alpha_7} & {\alpha_8} &{\alpha_9} & {\alpha_{10}} &{\alpha_{11}} &{\alpha_{12}} &{\alpha_{13}} &{\alpha_{14}} & {\alpha_{15}} \\
{0} & {0} &{0} &{1} &{0} &{0} &{1} &{0} &{0} &{0} &{1} &{0} &{0} &{1} &{0} & {0} \\
\end{array}
$$

which translates into the decimal number

$$
2^3+2^6+2^{10}+2^{13}=9288.
$$

We can thus encode a Slater determinant as a bit pattern.





## Operators in second quantization
With $N$ particles that can be distributed over $n$ single-particle states, the total number of Slater determinats (and defining thereby the dimensionality of the system) is

$$
\mathrm{dim}(\mathcal{H}) = \left(\begin{array}{c} n \\N\end{array}\right).
$$

The total number of bit patterns is $2^n$.




## Operators in second quantization
We assume again that we have at our disposal $n$ different single-particle orbits
$\alpha_0,\alpha_2,\dots,\alpha_{n-1}$ and that we can distribute  among these orbits $N\le n$ particles.
The ordering among these states is important as it defines the order of the creation operators.
We will write the determinant

$$
\Phi_{\Lambda} = a_{\alpha_3}^{\dagger} a_{\alpha_6}^{\dagger} a_{\alpha_{10}}^{\dagger} a_{\alpha_{13}}^{\dagger} |0\rangle,
$$

in a more compact way as

$$
\Phi_{3,6,10,13} = |0001001000100100\rangle.
$$

The action of a creation operator is thus

$$
a^{\dagger}_{\alpha_4}\Phi_{3,6,10,13} = a^{\dagger}_{\alpha_4}|0001001000100100\rangle=a^{\dagger}_{\alpha_4}a_{\alpha_3}^{\dagger} a_{\alpha_6}^{\dagger} a_{\alpha_{10}}^{\dagger} a_{\alpha_{13}}^{\dagger} |0\rangle,
$$

which becomes

$$
-a_{\alpha_3}^{\dagger} a^{\dagger}_{\alpha_4} a_{\alpha_6}^{\dagger} a_{\alpha_{10}}^{\dagger} a_{\alpha_{13}}^{\dagger} |0\rangle=-|0001101000100100\rangle.
$$

## Operators in second quantization
Similarly

$$
a^{\dagger}_{\alpha_6}\Phi_{3,6,10,13} = a^{\dagger}_{\alpha_6}|0001001000100100\rangle=a^{\dagger}_{\alpha_6}a_{\alpha_3}^{\dagger} a_{\alpha_6}^{\dagger} a_{\alpha_{10}}^{\dagger} a_{\alpha_{13}}^{\dagger} |0\rangle,
$$

which becomes

$$
-a^{\dagger}_{\alpha_4} (a_{\alpha_6}^{\dagger})^ 2 a_{\alpha_{10}}^{\dagger} a_{\alpha_{13}}^{\dagger} |0\rangle=0!
$$

This gives a simple recipe:  
* If one of the bits $b_j$ is $1$ and we act with a creation operator on this bit, we return a null vector

* If $b_j=0$, we set it to $1$ and return a sign factor $(-1)^l$, where $l$ is the number of bits set before bit $j$.





## Operators in second quantization
Consider the action of $a^{\dagger}_{\alpha_2}$ on various slater determinants:

$$
\begin{array}{ccc}
a^{\dagger}_{\alpha_2}\Phi_{00111}& = a^{\dagger}_{\alpha_2}|00111\rangle&=0\times |00111\rangle\\
a^{\dagger}_{\alpha_2}\Phi_{01011}& = a^{\dagger}_{\alpha_2}|01011\rangle&=(-1)\times |01111\rangle\\
a^{\dagger}_{\alpha_2}\Phi_{01101}& = a^{\dagger}_{\alpha_2}|01101\rangle&=0\times |01101\rangle\\
a^{\dagger}_{\alpha_2}\Phi_{01110}& = a^{\dagger}_{\alpha_2}|01110\rangle&=0\times |01110\rangle\\
a^{\dagger}_{\alpha_2}\Phi_{10011}& = a^{\dagger}_{\alpha_2}|10011\rangle&=(-1)\times |10111\rangle\\
a^{\dagger}_{\alpha_2}\Phi_{10101}& = a^{\dagger}_{\alpha_2}|10101\rangle&=0\times |10101\rangle\\
a^{\dagger}_{\alpha_2}\Phi_{10110}& = a^{\dagger}_{\alpha_2}|10110\rangle&=0\times |10110\rangle\\
a^{\dagger}_{\alpha_2}\Phi_{11001}& = a^{\dagger}_{\alpha_2}|11001\rangle&=(+1)\times |11101\rangle\\
a^{\dagger}_{\alpha_2}\Phi_{11010}& = a^{\dagger}_{\alpha_2}|11010\rangle&=(+1)\times |11110\rangle\\
\end{array}
$$

What is the simplest way to obtain the phase when we act with one annihilation(creation) operator
on the given Slater determinant representation?





## Operators in second quantization
We have an SD representation

$$
\Phi_{\Lambda} = a_{\alpha_0}^{\dagger} a_{\alpha_3}^{\dagger} a_{\alpha_6}^{\dagger} a_{\alpha_{10}}^{\dagger} a_{\alpha_{13}}^{\dagger} |0\rangle,
$$

in a more compact way as

$$
\Phi_{0,3,6,10,13} = |1001001000100100\rangle.
$$

The action of

$$
a^{\dagger}_{\alpha_4}a_{\alpha_0}\Phi_{0,3,6,10,13} = a^{\dagger}_{\alpha_4}|0001001000100100\rangle=a^{\dagger}_{\alpha_4}a_{\alpha_3}^{\dagger} a_{\alpha_6}^{\dagger} a_{\alpha_{10}}^{\dagger} a_{\alpha_{13}}^{\dagger} |0\rangle,
$$

which becomes

$$
-a_{\alpha_3}^{\dagger} a^{\dagger}_{\alpha_4} a_{\alpha_6}^{\dagger} a_{\alpha_{10}}^{\dagger} a_{\alpha_{13}}^{\dagger} |0\rangle=-|0001101000100100\rangle.
$$

## Operators in second quantization
The action

$$
a_{\alpha_0}\Phi_{0,3,6,10,13} = |0001001000100100\rangle,
$$

can be obtained by subtracting the logical sum (AND operation) of $\Phi_{0,3,6,10,13}$ and 
a word which represents only $\alpha_0$, that is

$$
|1000000000000000\rangle,
$$

from $\Phi_{0,3,6,10,13}= |1001001000100100\rangle$.

This operation gives $|0001001000100100\rangle$. 

Similarly, we can form $a^{\dagger}_{\alpha_4}a_{\alpha_0}\Phi_{0,3,6,10,13}$, say, by adding 
$|0000100000000000\rangle$ to $a_{\alpha_0}\Phi_{0,3,6,10,13}$, first checking that their logical sum
is zero in order to make sure that the state $\alpha_4$ is not already occupied.







## Operators in second quantization
It is trickier however to get the phase $(-1)^l$. 
One possibility is as follows
* Let $S_1$ be a word that represents the 1-bit to be removed and all others set to zero.

In the previous example $S_1=|1000000000000000\rangle$
* Define $S_2$ as the similar word that represents the bit to be added, that is in our case

$S_2=|0000100000000000\rangle$.
* Compute then $S=S_1-S_2$, which here becomes

$$
S=|0111000000000000\rangle
$$

* Perform then the logical AND operation of $S$ with the word containing

$$
\Phi_{0,3,6,10,13} = |1001001000100100\rangle,
$$

which results in $|0001000000000000\rangle$. Counting the number of 1-bits gives the phase.  Here you need however an algorithm for bitcounting.









## Bit counting


We include here a python program which may aid in this direction. It uses bit manipulation functions from <http://wiki.python.org/moin/BitManipulation>.

import math

"""
A simple Python class for Slater determinant manipulation
Bit-manipulation stolen from:

http://wiki.python.org/moin/BitManipulation
"""

# bitCount() counts the number of bits set (not an optimal function)

def bitCount(int_type):
    """ Count bits set in integer """
    count = 0
    while(int_type):
        int_type &= int_type - 1
        count += 1
    return(count)


# testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.

def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask) >> offset

# setBit() returns an integer with the bit at 'offset' set to 1.

def setBit(int_type, offset):
    mask = 1 << offset
    return(int_type | mask)

# clearBit() returns an integer with the bit at 'offset' cleared.

def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return(int_type & mask)

# toggleBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.

def toggleBit(int_type, offset):
    mask = 1 << offset
    return(int_type ^ mask)

# binary string made from number

def bin0(s):
    return str(s) if s<=1 else bin0(s>>1) + str(s&1)

def bin(s, L = 0):
    ss = bin0(s)
    if L > 0:
        return '0'*(L-len(ss)) + ss
    else:
        return ss
    
    

class Slater:
    """ Class for Slater determinants """
    def __init__(self):
        self.word = int(0)

    def create(self, j):
        print "c^+_" + str(j) + " |" + bin(self.word) + ">  = ",
        # Assume bit j is set, then we return zero.
        s = 0
        # Check if bit j is set.
        isset = testBit(self.word, j)
        if isset == 0:
            bits = bitCount(self.word & ((1<<j)-1))
            s = pow(-1, bits)
            self.word = setBit(self.word, j)

        print str(s) + " x |" + bin(self.word) + ">"
        return s
        
    def annihilate(self, j):
        print "c_" + str(j) + " |" + bin(self.word) + ">  = ",
        # Assume bit j is not set, then we return zero.
        s = 0
        # Check if bit j is set.
        isset = testBit(self.word, j)
        if isset == 1:
            bits = bitCount(self.word & ((1<<j)-1))
            s = pow(-1, bits)
            self.word = clearBit(self.word, j)

        print str(s) + " x |" + bin(self.word) + ">"
        return s



# Do some testing:

phi = Slater()
phi.create(0)
phi.create(1)
phi.create(2)
phi.create(3)

print


s = phi.annihilate(2)
s = phi.create(7)
s = phi.annihilate(0)
s = phi.create(200)

## Eigenvalue problems, basic definitions
Let us consider the matrix $\mathbf{A}$ of dimension $n$. The eigenvalues of
$\mathbf{A}$ are defined through the matrix equation

$$
\mathbf{A}\mathbf{x}^{(\nu)} = \lambda^{(\nu)}\mathbf{x}^{(\nu)},
$$

where $\lambda^{(\nu)}$ are the eigenvalues and $\mathbf{x}^{(\nu)}$ the
corresponding eigenvectors.
Unless otherwise stated, when we use the wording eigenvector we mean the
right eigenvector. The left eigenvalue problem is defined as

$$
\mathbf{x}^{(\nu)}_L\mathbf{A} = \lambda^{(\nu)}\mathbf{x}^{(\nu)}_L
$$

The above right eigenvector problem is equivalent to a set of $n$ equations with $n$ unknowns
$x_i$.





## Eigenvalue problems, basic definitions
The eigenvalue problem can be rewritten as

$$
\left( \mathbf{A}-\lambda^{(\nu)} \mathbf{I} \right) \mathbf{x}^{(\nu)} = 0,
$$

with $\mathbf{I}$ being the unity matrix. This equation provides
a solution to the problem if and only if the determinant
is zero, namely

$$
\left| \mathbf{A}-\lambda^{(\nu)}\mathbf{I}\right| = 0,
$$

which in turn means that the determinant is a polynomial
of degree $n$ in $\lambda$ and in general we will have 
$n$ distinct zeros.





## Eigenvalue problems, basic definitions
The eigenvalues of a matrix 
$\mathbf{A}\in {\mathbb{C}}^{n\times n}$
are thus the $n$ roots of its characteristic polynomial

$$
P(\lambda) = det(\lambda\mathbf{I}-\mathbf{A}),
$$

or

$$
P(\lambda)= \prod_{i=1}^{n}\left(\lambda_i-\lambda\right).
$$

The set of these roots is called the spectrum and is denoted as
$\lambda(\mathbf{A})$.
If $\lambda(\mathbf{A})=\left\{\lambda_1,\lambda_2,\dots ,\lambda_n\right\}$ then we have

$$
det(\mathbf{A})= \lambda_1\lambda_2\dots\lambda_n,
$$

and if we define the trace of $\mathbf{A}$ as

$$
Tr(\mathbf{A})=\sum_{i=1}^n a_{ii}
$$

then

$$
Tr(\mathbf{A})=\lambda_1+\lambda_2+\dots+\lambda_n.
$$

## Abel-Ruffini Impossibility Theorem
The *Abel-Ruffini* theorem (also known as Abel's impossibility theorem) 
states that there is no general solution in radicals to polynomial equations of degree five or higher.

The content of this theorem is frequently misunderstood. It does not assert that higher-degree polynomial equations are unsolvable. 
In fact, if the polynomial has real or complex coefficients, and we allow complex solutions, then every polynomial equation has solutions; this is the fundamental theorem of algebra. Although these solutions cannot always be computed exactly with radicals, they can be computed to any desired degree of accuracy using numerical methods such as the Newton-Raphson method or Laguerre method, and in this way they are no different from solutions to polynomial equations of the second, third, or fourth degrees.

The theorem only concerns the form that such a solution must take. The content of the theorem is 
that the solution of a higher-degree equation cannot in all cases be expressed in terms of the polynomial coefficients with a finite number of operations of addition, subtraction, multiplication, division and root extraction. Some polynomials of arbitrary degree, of which the simplest nontrivial example is the monomial equation $ax^n = b$, are always solvable with a radical.





## Abel-Ruffini Impossibility Theorem

The *Abel-Ruffini* theorem says that there are some fifth-degree equations whose solution cannot be so expressed. 
The equation $x^5 - x + 1 = 0$ is an example. Some other fifth degree equations can be solved by radicals, 
for example $x^5 - x^4 - x + 1 = 0$. The precise criterion that distinguishes between those equations that can be solved 
by radicals and those that cannot was given by Galois and is now part of Galois theory: 
a polynomial equation can be solved by radicals if and only if its Galois group is a solvable group.

Today, in the modern algebraic context, we say that second, third and fourth degree polynomial 
equations can always be solved by radicals because the symmetric groups $S_2, S_3$ and $S_4$ are solvable groups, 
whereas $S_n$ is not solvable for $n \ge 5$.





## Eigenvalue problems, basic definitions
In the present discussion we assume that our matrix is real and symmetric, that is 
$\mathbf{A}\in {\mathbb{R}}^{n\times n}$.
The matrix $\mathbf{A}$ has $n$ eigenvalues
$\lambda_1\dots \lambda_n$ (distinct or not). Let $\mathbf{D}$ be the
diagonal matrix with the eigenvalues on the diagonal

$$
\mathbf{D}=    \left( \begin{array}{ccccccc} \lambda_1 & 0 & 0   & 0    & \dots  &0     & 0 \\
                                0 & \lambda_2 & 0 & 0    & \dots  &0     &0 \\
                                0   & 0 & \lambda_3 & 0  &0       &\dots & 0\\
                                \dots  & \dots & \dots & \dots  &\dots      &\dots & \dots\\
                                0   & \dots & \dots & \dots  &\dots       &\lambda_{n-1} & \\
                                0   & \dots & \dots & \dots  &\dots       &0 & \lambda_n
             \end{array} \right).
$$

If $\mathbf{A}$ is real and symmetric then there exists a real orthogonal matrix $\mathbf{S}$ such that

$$
\mathbf{S}^T \mathbf{A}\mathbf{S}= \mathrm{diag}(\lambda_1,\lambda_2,\dots ,\lambda_n),
$$

and for $j=1:n$ we have $\mathbf{A}\mathbf{S}(:,j) = \lambda_j \mathbf{S}(:,j)$.





## Eigenvalue problems, basic definitions
To obtain the eigenvalues of $\mathbf{A}\in {\mathbb{R}}^{n\times n}$,
the strategy is to
perform a series of similarity transformations on the original
matrix $\mathbf{A}$, in order to reduce it either into a  diagonal form as above
or into a  tridiagonal form. 

We say that a matrix $\mathbf{B}$ is a similarity
transform  of  $\mathbf{A}$ if

$$
\mathbf{B}= \mathbf{S}^T \mathbf{A}\mathbf{S}, \hspace{1cm} \mathrm{where} \hspace{1cm}  \mathbf{S}^T\mathbf{S}=\mathbf{S}^{-1}\mathbf{S} =\mathbf{I}.
$$

The importance of a similarity transformation lies in the fact that
the resulting matrix has the same
eigenvalues, but the eigenvectors are in general different.





## Eigenvalue problems, basic definitions
To prove this we
start with  the eigenvalue problem and a similarity transformed matrix $\mathbf{B}$.

$$
\mathbf{A}\mathbf{x}=\lambda\mathbf{x} \hspace{1cm} \mathrm{and}\hspace{1cm} 
    \mathbf{B}= \mathbf{S}^T \mathbf{A}\mathbf{S}.
$$

We multiply the first equation on the left by $\mathbf{S}^T$ and insert
$\mathbf{S}^{T}\mathbf{S} = \mathbf{I}$ between $\mathbf{A}$ and $\mathbf{x}$. Then we get

<!-- Equation labels as ordinary links -->
<div id="_auto2"></div>

$$
\begin{equation}
   (\mathbf{S}^T\mathbf{A}\mathbf{S})(\mathbf{S}^T\mathbf{x})=\lambda\mathbf{S}^T\mathbf{x} ,
\label{_auto2} \tag{3}
\end{equation}
$$

which is the same as

$$
\mathbf{B} \left ( \mathbf{S}^T\mathbf{x} \right ) = \lambda \left (\mathbf{S}^T\mathbf{x}\right ).
$$

The variable  $\lambda$ is an eigenvalue of $\mathbf{B}$ as well, but with
eigenvector $\mathbf{S}^T\mathbf{x}$.





## Eigenvalue problems, basic definitions
The basic philosophy is to
 * Either apply subsequent similarity transformations (direct method) so that

<!-- Equation labels as ordinary links -->
<div id="_auto3"></div>

$$
\begin{equation}
   \mathbf{S}_N^T\dots \mathbf{S}_1^T\mathbf{A}\mathbf{S}_1\dots \mathbf{S}_N=\mathbf{D} ,
\label{_auto3} \tag{4}
\end{equation}
$$

* Or apply subsequent similarity transformations so that $\mathbf{A}$ becomes tridiagonal (Householder) or upper/lower triangular (the *QR* method to be discussed later). 

 * Thereafter, techniques for obtaining eigenvalues from tridiagonal matrices can be used.

 * Or use so-called power methods

 * Or use iterative methods (Krylov, Lanczos, Arnoldi). These methods are popular for huge matrix problems.






## Discussion of  methods for eigenvalues
**The general overview.**


One speaks normally of two main approaches to solving the eigenvalue problem.
 * The first is the formal method, involving determinants and the  characteristic polynomial. This proves how many eigenvalues  there are, and is the way most of you learned about how to solve the eigenvalue problem, but for matrices of dimensions greater than 2 or 3, it is rather impractical.

 * The other general approach is to use similarity or unitary tranformations  to reduce a matrix to diagonal form. This is normally done in two steps: first reduce to for example a *tridiagonal* form, and then to diagonal form. The main algorithms we will discuss in detail, Jacobi's and  Householder's  (so-called direct method) and Lanczos algorithms (an iterative method), follow this methodology.





## Eigenvalues methods
Direct or non-iterative methods  require for matrices of dimensionality $n\times n$ typically $O(n^3)$ operations. These methods are normally called standard methods and are used for dimensionalities
$n \sim 10^5$ or smaller. A brief historical overview  

<table border="1">
<thead>
<tr><th align="center">    Year   </th> <th align="center">    $n$     </th> <th align="center">                 </th> </tr>
</thead>
<tbody>
<tr><td align="center">   1950           </td> <td align="center">   $n=20$          </td> <td align="center">   (Wilkinson)          </td> </tr>
<tr><td align="center">   1965           </td> <td align="center">   $n=200$         </td> <td align="center">   (Forsythe et al.)    </td> </tr>
<tr><td align="center">   1980           </td> <td align="center">   $n=2000$        </td> <td align="center">   Linpack              </td> </tr>
<tr><td align="center">   1995           </td> <td align="center">   $n=20000$       </td> <td align="center">   Lapack               </td> </tr>
<tr><td align="center">   This decade    </td> <td align="center">   $n\sim 10^5$    </td> <td align="center">   Lapack               </td> </tr>
</tbody>
</table>
shows that in the course of 60 years the dimension that  direct diagonalization methods can handle  has increased by almost a factor of
$10^4$ (note this is for serial versions). However, it pales beside the progress achieved by computer hardware, from flops to petaflops, a factor of almost $10^{15}$. We see clearly played out in history the $O(n^3)$ bottleneck  of direct matrix algorithms.

Sloppily speaking, when  $n\sim 10^4$ is cubed we have $O(10^{12})$ operations, which is smaller than the $10^{15}$ increase in flops.





## Discussion of methods for eigenvalues
If the matrix to diagonalize is large and sparse, direct methods simply become impractical, 
also because
many of the direct methods tend to destroy sparsity. As a result large dense matrices may arise during the diagonalization procedure.  The idea behind iterative methods is to project the 
$n-$dimensional problem in smaller spaces, so-called Krylov subspaces. 
Given a matrix $\mathbf{A}$ and a vector $\mathbf{v}$, the associated Krylov sequences of vectors
(and thereby subspaces) 
$\mathbf{v}$, $\mathbf{A}\mathbf{v}$, $\mathbf{A}^2\mathbf{v}$, $\mathbf{A}^3\mathbf{v},\dots$, represent
successively larger Krylov subspaces. 

<table border="1">
<thead>
<tr><th align="center">           Matrix           </th> <th align="center">$\mathbf{A}\mathbf{x}=\mathbf{b}$</th> <th align="center">$\mathbf{A}\mathbf{x}=\lambda\mathbf{x}$</th> </tr>
</thead>
<tbody>
<tr><td align="left">   $\mathbf{A}=\mathbf{A}^*$       </td> <td align="left">   Conjugate gradient                   </td> <td align="left">   Lanczos                                     </td> </tr>
<tr><td align="left">   $\mathbf{A}\ne \mathbf{A}^*$    </td> <td align="left">   GMRES etc                            </td> <td align="left">   Arnoldi                                     </td> </tr>
</tbody>
</table>





## Eigenvalues and Lanczos' method
Basic features with a real symmetric matrix (and normally huge $n> 10^6$ and sparse) 
$\hat{A}$ of dimension $n\times n$:

* Lanczos' algorithm generates a sequence of real tridiagonal matrices $T_k$ of dimension $k\times k$ with $k\le n$, with the property that the extremal eigenvalues of $T_k$ are progressively better estimates of $\hat{A}$' extremal eigenvalues.* The method converges to the extremal eigenvalues.

* The similarity transformation is

$$
\hat{T}= \hat{Q}^{T}\hat{A}\hat{Q},
$$

with the first vector $\hat{Q}\hat{e}_1=\hat{q}_1$.

We are going to solve iteratively

$$
\hat{T}= \hat{Q}^{T}\hat{A}\hat{Q},
$$

with the first vector $\hat{Q}\hat{e}_1=\hat{q}_1$.
We can write out the matrix $\hat{Q}$ in terms of its column vectors

$$
\hat{Q}=\left[\hat{q}_1\hat{q}_2\dots\hat{q}_n\right].
$$

## Eigenvalues and Lanczos' method, tridiagonal matrix
The matrix

$$
\hat{T}= \hat{Q}^{T}\hat{A}\hat{Q},
$$

can be written as

$$
\hat{T} = \left(\begin{array}{cccccc}
                           \alpha_1& \beta_1 & 0 &\dots   & \dots &0 \\
                           \beta_1 & \alpha_2 & \beta_2 &0 &\dots &0 \\
                           0& \beta_2 & \alpha_3 & \beta_3 & \dots &0 \\
                           \dots& \dots   & \dots &\dots   &\dots & 0 \\
                           \dots&   &  &\beta_{n-2}  &\alpha_{n-1}& \beta_{n-1} \\
                           0&  \dots  &\dots  &0   &\beta_{n-1} & \alpha_{n} \\
                      \end{array} \right)
$$

## Eigenvalues and Lanczos' method, tridiagonal and orthogonal matrices
Using the fact that

$$
\hat{Q}\hat{Q}^T=\hat{I},
$$

we can rewrite

$$
\hat{T}= \hat{Q}^{T}\hat{A}\hat{Q},
$$

as

$$
\hat{Q}\hat{T}= \hat{A}\hat{Q}.
$$

## Eigenvalues and Lanczos' method
If we equate columns

$$
\hat{T} = \left(\begin{array}{cccccc}
        \alpha_1& \beta_1 & 0 &\dots   & \dots &0 \\
        \beta_1 & \alpha_2 & \beta_2 &0 &\dots &0 \\
        0& \beta_2 & \alpha_3 & \beta_3 & \dots &0 \\
        \dots& \dots   & \dots &\dots   &\dots & 0 \\
        \dots&   &  &\beta_{n-2}  &\alpha_{n-1}& \beta_{n-1} \\
        0&  \dots  &\dots  &0   &\beta_{n-1} & \alpha_{n} \\
        \end{array} \right)
$$

we obtain

$$
\hat{A}\hat{q}_k=\beta_{k-1}\hat{q}_{k-1}+\alpha_k\hat{q}_k+\beta_k\hat{q}_{k+1}.
$$

## Eigenvalues and Lanczos' method, defining the Lanczos' vectors
We have thus

$$
\hat{A}\hat{q}_k=\beta_{k-1}\hat{q}_{k-1}+\alpha_k\hat{q}_k+\beta_k\hat{q}_{k+1},
$$

with $\beta_0\hat{q}_0=0$ for $k=1:n-1$. Remember that the vectors $\hat{q}_k$  are orthornormal and this implies

$$
\alpha_k=\hat{q}_k^T\hat{A}\hat{q}_k,
$$

and these vectors are called Lanczos vectors.




## Eigenvalues and Lanczos' method, basic steps
We have thus

$$
\hat{A}\hat{q}_k=\beta_{k-1}\hat{q}_{k-1}+\alpha_k\hat{q}_k+\beta_k\hat{q}_{k+1},
$$

with $\beta_0\hat{q}_0=0$ for $k=1:n-1$ and

$$
\alpha_k=\hat{q}_k^T\hat{A}\hat{q}_k.
$$

If

$$
\hat{r}_k=(\hat{A}-\alpha_k\hat{I})\hat{q}_k-\beta_{k-1}\hat{q}_{k-1},
$$

is non-zero, then

$$
\hat{q}_{k+1}=\hat{r}_{k}/\beta_k,
$$

with $\beta_k=\pm ||\hat{r}_{k}||_2$.