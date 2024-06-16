# Summary

Using Github Actions to integrate the most simple flow of CI/CD pipelines

- Setup the environment
- Build the code
- Test it with unit test
- Deploy to Github page with predefined action

# Setup

## Setup the repo, github page and basic flows

[Deploying React Apps to Github Pages with Github Actions - DEV Community](https://dev.to/codeparrot/deploying-react-apps-to-github-pages-with-github-actions-5gja)

- The workflow folder must be `./github/workflows`
- If having issues with permission:
    - Check the read write permissions in Github Repo settings → Actions → General tab
    - Check if the token in **Github Repo settings → Secrets** working. Might need to create a new PERSONAL_TOKEN and update the workflow file
    - Update versions of actions if needed
- To prevent the next step from running, use`if condition`
    
    ```swift
    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3
      if: success()
    ```
    

## Setup the test

[TypeScript Unit Testing 101: A Developer's Guide - AI-driven E2E automation with code-like flexibility for your most resilient tests (testim.io)](https://www.testim.io/blog/typescript-unit-testing-101/)

- If getting `zsh: command not found` when running `jest`: Use command `./node_modules/.bin/jest` . Better to just use this in the test script in `package.json`
- If getting `module is not defined in ES module scope` : convert `jest.config.js` to be `jest.config.json`

## Setup Test Reporter

[Using Reporter in Jest Framework (askui.com)](https://www.askui.com/blog-posts/generating-reports-for-your-automation-run)

- Types of report for `jest`
    - “default”: the template that we often sees when running tests without any configs
    - “jest-junit”: the template that is commonly used, needs to install to use
        - `npm install -g jest-junit`
        - Can specify the reporter in `jest.config.json` . Avoid reporter config duplications since there are 3 ways to set the config

[Test Reporter · Actions · GitHub Marketplace](https://github.com/marketplace/actions/test-reporter)

- The `path` and `reporter` config for the action should match the `path` in the `jest.config.json`

## References
- [Github Action docs](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
- [gh-pages action docs](https://github.com/peaceiris/actions-gh-pages#readme)
- [jest docs](https://jestjs.io/docs/configuration#reporters-arraymodulename--modulename-options)
- [jest-junit docs](https://github.com/jest-community/jest-junit)
- [Test reporter docs](https://github.com/marketplace/actions/test-reporter)
