# Hybrid Sort Energy Project

![Energy Sorting Hero](energy_sorting_hero.png)

A comprehensive study of the energy efficiency of various hybrid sorting algorithms. This project measures the power consumption and runtime of sorting implementations using Intel Power Gadget.

## 🚀 Overview

The goal of this research is to identify sorting strategies that minimize the carbon footprint of data processing. By analyzing energy consumption in Joules rather than just CPU cycles, we gain a holistic view of algorithm performance.

## 📊 Portfolio

The project includes a hosted portfolio demonstrating the findings:
[View Portfolio](https://SYuskanth.github.io/hybrid_sort_energy_project/)

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Libraries**: Pandas, NumPy, Intel Power Gadget
- **Web**: HTML5, Vanilla CSS3 (Glassmorphism design)

## 🧪 Algorithms Compared

- **Timsort**: Optimized for real-world data.
- **Introsort**: Stable O(n log n) performance.
- **Dual Pivot Quicksort**: Enhanced quicksort strategy.
- **Hybrid Quick-Insertion**: High-speed hybrid approach.
- **Recombinant Sort**: Experimental multi-strategy hybrid.

## 📈 Methodology

The experiment runs each algorithm across multiple data sizes (1k to 1M elements), repeating each test 10 times to ensure statistical accuracy. Energy is measured using the Intel Power Gadget API, logging Processor Power (Watts) and calculating total energy (Joules).

## 📄 License

MIT License
