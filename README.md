# Mathing 🎲🔢

This repository contains some of my research projects and scripts, mostly done just for fun. The initial focus here is cousin primes, but I’m exploring chaos theory and nonlinear dynamics as well.


[Here](https://medium.com/science-spectrum/the-hardy-littlewood-conjectures-exploring-the-asymptotic-densities-of-prime-pairs-f95d03cb58a0) is a link to a Medium article I wrote on the Hardy-Littlewood Conjectures. It showcases some of the visualizations created in this repository.

### Asymptotic Density of Cousin Primes
One project I'm diving into is looking at the asymptotic density of cousin primes. Cousin primes are pairs of primes that differ by 4 (for example, 3 and 7). I recently wrote a Python script that plots how the density of these primes changes as we go higher and higher in the prime number sequence.

Here's a quick visual of the asymptotic density of cousin primes up to 1000:

![{C8B5B4AD-0F27-4F18-A6EC-723BA89B063A}](https://github.com/user-attachments/assets/9b16a8f7-b607-4e22-bd8e-10796bc06795)

Note that the asymptotic density of the cousin primes is expected to be the same as that of the twin primes, according to the Hardy-Littlewood conjecture.

## How to Use the Scripts
Clone this repo and check out the Python scripts. You’ll need `sympy` and `matplotlib` to run most of them. Here’s how to set it up:

```bash
git clone https://github.com/your-username/mathing.git
cd mathing
pip install -r requirements.txt
