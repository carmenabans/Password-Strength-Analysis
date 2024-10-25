# Password Strength Study

## Introduction
This project explores the strength of various types of passwords by generating and empirically analyzing datasets of different complexities. The primary goal is to understand the effort required to crack different password types, using various strategies to assess password robustness against cracking attempts.

## Context
Password security is a critical area of study in cybersecurity, as weak passwords can pose significant risks to personal and organizational security. This study aims to examine the difficulty of cracking passwords of various types and complexities. Using **John the Ripper (JtR)**, we experimented with multiple cracking strategies on datasets with controlled variations to evaluate the effectiveness of common password-cracking methods.

## Datasets
To analyze password-cracking strategies, we generated five sets of datasets, each with five collections of 100 passwords. Each set represents a different complexity level and contains passwords generated as follows:

1. **Lowercase Letters Only**: Passwords composed exclusively of lowercase letters.
2. **Uppercase Letters Only**: Passwords composed exclusively of uppercase letters.
3. **Numeric Only**: Passwords composed exclusively of numbers.
4. **Alphanumeric with Symbols**: Passwords that include a mix of uppercase and lowercase letters, numbers, and symbols.
5. **Dictionary-Based**: Passwords generated using words from a dictionary, simulating commonly used password patterns.

## Methodology
Passwords were hashed using `md5crypt` to simulate stored password security, and five different cracking strategies were applied in **John the Ripper (JtR)**, including:

1. **Dictionary Attack**: This approach uses a pre-defined wordlist along with JtR’s rule-based modifications.
2. **Single Crack Mode**: Though less applicable for randomly generated passwords, it uses account-specific information for cracking, which is more efficient than wordlists in some real-world scenarios.
3. **Incremental Mode**: Standard brute-force attack, testing all possible password combinations.
4. **External Mode**: A custom mode that allows additional password generation methods using C code extensions in JtR.

### Custom Dictionaries
Three specific wordlists were created for targeted cracking:
- **Wordlist_1**: Targeted towards lowercase and uppercase password sets, containing 6,000 random letter-based entries.
- **Wordlist_2**: For alphanumeric sets, including a mix of numbers and ASCII symbols.
- **Rockyou-75**: A popular dataset with over 59,000 common passwords used for dictionary-based datasets.

## Key Features
- **Dataset Generation**: Python scripts generate password datasets with controlled complexity levels.
- **Cracking Strategies**: Implemented five cracking methods in JtR, tailored for each dataset type.
- **Performance Analysis**: Detailed metrics for each strategy, including:
  - Percentage of cracked passwords.
  - Average and median cracking time per password.
  - Total execution time, with a limit set to 90 minutes.

## Results and Analysis
Results were evaluated for each strategy across datasets. Key metrics include the success rate of cracking attempts, average and median times for each password type, and observations on method efficiency. Summary tables and visualizations were created to aid in comparative analysis.

### Key Findings
- **Brute Force**: Effective for short passwords; increasingly ineffective for longer, complex passwords.
- **Dictionary Attacks**: Fast and efficient if a relevant wordlist is available.
- **Mixed Complexity Passwords**: The more unique and varied the character types, the more secure the password.
- **Number-Only Passwords**: These were the most vulnerable, even for lengths greater than six characters.

Graphs highlight the performance of each method, showing that while brute force guarantees success given enough time, dictionary-based attacks are faster for common passwords.

## Technologies
- **Python**: For generating password datasets and analyzing results.
- **John the Ripper**: Tool for password cracking.
- **Kali Linux**: Operating system used for running security tools and managing the cracking environment.

## Team
- Carmen Abans Maciel: https://github.com/carmenabans
- Noelia Hernández Rodríguez: https://github.com/Noeliahr10 


