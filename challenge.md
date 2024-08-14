# Github Profile Analysis

## Objective
Evaluate the technical skills of the candidate in backend development, reusable code creation, technical documentation interpretation, rate limit handling, and  data processing using third-party integrations.

## General Instructions
- You can use any backend programming language you are comfortable with (e.g., Node.js, Python, Java, etc.).
- You may use GitHub API integration either via REST or GraphQL, but the output API must be REST.
- Your code needs to be documented and explaines where necessary.
- Include a `README.md` file with instructions on how to run your solution and any important details.

## Challenge Description

Imagine that you are part of a fictional company that is building an advanced analytics platform for developers' GitHub profiles. Your task is to create a system that can extract meaningful insights from a user's GitHub profile. By evaluating their open-source contributions, your system will provide valuable information about their coding practices, preferred languages, and overall activity.

### Part 1: RESTful API and Data Processing

You need to create an endpoint that can be queried to get insights into a GitHub profile by passing the GitHub username as a parameter. This endpoint will retrieve detailed insights from a specific GitHub user's profile. The response should include the following information:

- **Top 3 most used programming languages:** Determine the most common languages used across the user's repositories.
- **Repositories with the most merged pull requests:** Identify the repositories where the user has had the most pull requests accepted.
- **Contributions in the last 6 months:** Count the total number of pull requests, issues, and commits the user has made in the last 6 months, and display these numbers month by month in an array.
- **Days and time slots of highest activity:** Analyze the user's events to determine the days of the week and time slots (morning, afternoon, evening) when the user is most active.

> The endpoint should be structured as follows: `GET /user-insights/:username`

### Part 2: Integration and Rate Limit Handling

- Use the GitHub API to implement the operations needed for the insights. Authentication using OAuth or personal tokens may be required.
- Ensure you handle GitHub's rate limits appropriately. Your API should be able to handle rate limit errors and implement a retry logic with exponential backoff.

### Part 3: Open/Closed Principle (OCP)

- Structure your code in a way that makes it easy to include new metrics in the future without modifying existing code. This means that if a new metric is required in the future, a new programmer should be able to add it through extension rather than modification.

### Part 4: Documentation and Tests

- Use Swagger or a similar tool to document your API.
- Include a brief explanation of each endpoint and the possible response codes.
- Write unit and integration tests for the main endpoints of your API.
- Ensure the tests cover the most important cases, including validations, error handling, and retry logic for rate limits.

### Example GitHub Profiles

- **Profiles with Many Repositories:**
  - [torvalds](https://github.com/torvalds) (Linus Torvalds)
  - [mojombo](https://github.com/mojombo) (Tom Preston-Werner)

- **Profiles with Few Repositories:**
  - [dhh](https://github.com/dhh) (David Heinemeier Hansson)
  - [tenderlove](https://github.com/tenderlove) (Aaron Patterson)
 
## Bonus

**Infer developer most user Languages from commits instead of entire repo:**
- Additionally, you may infer the languages used in the user’s commits instead of relying on the overall repository languages (since a repository could contain multiple languages, and the user may not have contributed to all of them).
- Analyze the extensions of files modified in the user’s commits to determine the most frequently used languages in their contributions.
- This functionality should be implemented in a way that makes it easy to add more file extensions and corresponding languages in the future.