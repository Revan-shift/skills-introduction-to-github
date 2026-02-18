{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15df5cb1-fec0-413a-bb39-71747bf6e983",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Task 3\n",
    "def to_float(s):\n",
    "    \"\"\"\n",
    "    Attempts to convert a string to a float.\n",
    "    Returns the float value if successful, otherwise returns None.\n",
    "    \"\"\"\n",
    "    try:\n",
    "        return float(s)\n",
    "    except (ValueError, TypeError):\n",
    "        return None\n",
    "\n",
    "def clean_string(s):\n",
    "    \"\"\"\n",
    "    Removes leading/trailing whitespace and converts string to lowercase.\n",
    "    \"\"\"\n",
    "    if isinstance(s, str):\n",
    "        return s.strip().lower()\n",
    "    return None\n",
    "\n",
    "# --- Testing the functions ---\n",
    "if __name__ == \"__main__\":\n",
    "    # Create a list of at least five test inputs\n",
    "    test_inputs = [\"  12.5  \", \"99\", \"not_a_number\", \"\", \"  DATA Science  \"]\n",
    "\n",
    "    # Apply each function to the list\n",
    "    float_outputs = [to_float(item) for item in test_inputs]\n",
    "    clean_outputs = [clean_string(item) for item in test_inputs]\n",
    "\n",
    "    # Display results\n",
    "    print(f\"Original Inputs: {test_inputs}\")\n",
    "    print(f\"Float Results:   {float_outputs}\")\n",
    "    print(f\"Cleaned Results: {clean_outputs}\")"
   ]
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
