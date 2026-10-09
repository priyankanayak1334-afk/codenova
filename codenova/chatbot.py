{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "132fd5fb-6dc3-488c-9e11-9f83f26c6573",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bot: Hello! I am Nova, your virtual customer support assistant.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Bot: Before we begin, what is your name?  Priyanka\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bot: Nice to meet you, Priyanka! Type 'help' to see what I can do, or 'bye' to exit.\n"
     ]
    }
   ],
   "source": [
    "print(\"Bot: Hello! I am Nova, your virtual customer support assistant.\")\n",
    "user_name = input(\"Bot: Before we begin, what is your name? \")\n",
    "print(f\"Bot: Nice to meet you, {user_name}! Type 'help' to see what I can do, or 'bye' to exit.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "98d469d3-216b-4178-a71f-9d286d019377",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Priyanka:  hours \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bot: Our official support hours are Monday to Friday, 9:00 AM to 6:00 PM.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Priyanka:  bye \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bot: Goodbye, Priyanka! Have a wonderful day ahead.\n"
     ]
    }
   ],
   "source": [
    "# Start a continuous conversation loop\n",
    "while True:\n",
    "    # Get input from the user\n",
    "    user_input = input(f\"{user_name}: \")\n",
    "    \n",
    "    # Clean up the input (remove extra spaces and make it lowercase)\n",
    "    clean_input = user_input.strip().lower()\n",
    "    \n",
    "    # 1. Check for Exit command\n",
    "    if \"bye\" in clean_input or \"exit\" in clean_input:\n",
    "        print(f\"Bot: Goodbye, {user_name}! Have a wonderful day ahead.\")\n",
    "        break  # Safely stops the running notebook cell from hanging\n",
    "        \n",
    "    # 2. Check for Greetings\n",
    "    elif \"hello\" in clean_input or \"hi\" in clean_input or \"hey\" in clean_input:\n",
    "        print(f\"Bot: Hello again, {user_name}! How can I help you today?\")\n",
    "        \n",
    "    # 3. Check for Help menu\n",
    "    elif \"help\" in clean_input or \"support\" in clean_input or \"options\" in clean_input:\n",
    "        print(\"Bot: I can help you with the following topics:\")\n",
    "        print(\"   - Type 'hours' to see our operational timings.\")\n",
    "        print(\"   - Type 'contact' to get our support email.\")\n",
    "        print(\"   - Type 'internship' to learn about Code-A-Nova.\")\n",
    "        \n",
    "    # 4. Check for Business Hours\n",
    "    elif \"hours\" in clean_input or \"time\" in clean_input:\n",
    "        print(\"Bot: Our official support hours are Monday to Friday, 9:00 AM to 6:00 PM.\")\n",
    "        \n",
    "    # 5. Check for Contact Info\n",
    "    elif \"contact\" in clean_input or \"email\" in clean_input:\n",
    "        print(\"Bot: You can reach our human support team at codeanova26@gmail.com.\")\n",
    "        \n",
    "    # 6. Check for Company Info\n",
    "    elif \"internship\" in clean_input or \"code-a-nova\" in clean_input:\n",
    "        print(f\"Bot: Code-A-Nova focuses on project-based internships to bridge academic gaps!\")\n",
    "        \n",
    "    # 7. Fallback for completely unknown inputs\n",
    "    else:\n",
    "        print(f\"Bot: I'm sorry, {user_name}, I didn't quite understand that. Type 'help' for options.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5a41177-7c24-471b-8b85-877eb2e423fd",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
