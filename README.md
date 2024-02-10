# ModeratorProgram-TestFramework

The Moderator Program, `moderator.py` is a sophisticated Python tool for automating online forum moderation, designed to validate community discussions. Accompanying this program is a Testing Suite, comprising `test.py` and `test_functions.py`, which rigorously evaluates the moderation program's functionality.

## How it's Made

**Moderator Program**:
- **Input Validation**: Validates inputs such as names and date-time strings against predefined criteria.
- **CLI (Command-Line Interface)**: Facilitates the execution of moderation tasks via command-line arguments.
- **Content Moderation**: Employs string processing to censor inappropriate content.
- **Data Organisation**: Analyzes and ranks users based on their contributions.

**Testing Suite**:
- **`test_functions.py`**: Contains core functions like `is_valid_name` and `is_chronological` for validating names and date-time strings.
- **`test.py`**: Utilizes the functions from `test_functions.py` to conduct black box testing on the Moderator Program, ensuring its robustness and reliability.

## Optimisations
Refinements in input validation and content censoring have been made for enhanced performance. Regular expressions have been leveraged to simplify and speed up content moderation processes.

## Lessons Learned
Key takeaways include the significance of thorough input validation, the benefits of continuous optimization, and the essential role of backend functionalities in improving user experiences in online communities.

## Running the Program

**Moderator Program**:
1. Download the program files to a local directory.
2. Open a terminal or command prompt and navigate to the program's directory.
3. Run the program using the command:
   ```
   python3 moderator.py -task <task> -log <log_file> -forum <forum_file> -words <words_file> -people <people_file>
   ```
Adjust `<task>`, `<log_file>`, `<forum_file>`, `<words_file>`, and `<people_file>` to your specific requirements.

**Testing Suite**:
Run `test.py` after ensuring `test_functions.py` is in the same directory to validate the Moderator Program's functionalities.


## Examples
Here are a few more projects from my portfolio:
- [Abalone Age Prediction Conservation Model](https://github.com/christy511/AbaloneAgePrediction-ConservationModels):
A model to predict the age of abalone through machine learning.
- [Customised Fitness Regimen](https://github.com/christy511/Customised-Fitness-Regimen/tree/main)
Adaptive workout recommendation engine using conditional logic and user data.
