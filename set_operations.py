{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b94cb2e3-ee7b-43d6-ba55-8d161cd5311f",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8}\n",
      "Intersection of E and N is {2, 4}\n",
      "Difference of E and N is {0, 8, 6}\n",
      "Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}\n"
     ]
    }
   ],
   "source": [
    "# Define two sets\n",
    "E = {0, 2, 4, 6, 8}\n",
    "N = {1, 2, 3, 4, 5}\n",
    "\n",
    "# Perform set operations\n",
    "union = E | N\n",
    "intersection = E & N\n",
    "difference = E - N\n",
    "symmetric_difference = E ^ N\n",
    "\n",
    "# Print the results\n",
    "print(\"Union of E and N is\", union)\n",
    "print(\"Intersection of E and N is\", intersection)\n",
    "print(\"Difference of E and N is\", difference)\n",
    "print(\"Symmetric difference of E and N is\", symmetric_difference)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab0b67c2-a9f2-4653-b0f7-08a68a502bf2",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-panel-2023.05-py310",
   "language": "python",
   "name": "conda-env-anaconda-panel-2023.05-py310-py"
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
