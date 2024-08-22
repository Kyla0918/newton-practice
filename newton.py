{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "78ca8c37-498c-4af8-98e8-401569ad418c",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'math' has no attribute 'derivative'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[5], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmath\u001b[39;00m\n\u001b[0;32m----> 2\u001b[0m help(\u001b[43mmath\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mderivative\u001b[49m)\n",
      "\u001b[0;31mAttributeError\u001b[0m: module 'math' has no attribute 'derivative'"
     ]
    }
   ],
   "source": [
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae10fa7b-889b-4cf9-a0a4-d60e89c3f4e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def first_derivative(f, x, h = 1e-10):\n",
    "    return (f(x + h) - f(x)) / h\n",
    "    \n",
    "def second_derivative(f, x, h = 1e-10):\n",
    "    return (first_derivative(f, x + h) - first_derivative(f, x)) / h\n",
    "    \n",
    "x = x0\n",
    "iterations = 0\n",
    "\n",
    "def optimize(f, x):\n",
    "    \n",
    "    while iterations < max_iter:\n",
    "        fx = f(x)\n",
    "        dx = first_derivative(f, x)\n",
    "        d2x = second_derivative(f, x)\n",
    "        \n",
    "        if abs(dx) < epsilon:\n",
    "            return x, fx, iterations\n",
    "        \n",
    "        if abs(dx) < epsilon:\n",
    "        return x, fx, i\n",
    "        \n",
    "        x = x - dx / d2x\n",
    "    \n",
    "    return x, f(x), max_iter\n",
    "\n",
    "x_optimal, f_optimal, iterations = newton_method(f, x0=0)\n",
    "print(f\"Optimal x: {x_optimal}\")\n",
    "print(f\"Optimal f(x): {f_optimal}\")\n",
    "print(f\"Number of iterations: {iterations}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "20974ebc-d8aa-416d-93d3-7d4ab275259e",
   "metadata": {},
   "outputs": [],
   "source": [
    "git config --global user.name \"XIyue Liang\"\n",
    "git config --global user.email \"xiyue_liang@berkeley.edu\"\n",
    "\n",
    "git config --global color.ui \"auto\"\n",
    "\n",
    "git config --global pull.rebase false"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2699c742-73c0-42a2-9e07-acf6eea36afc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
