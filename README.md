# abc-python

The goal of the project is to provide you with the tools to make basic code quality control of your own Python project.

All linters are wrapped in [pre-commit](https://pre-commit.com/) hooks, so all you need is to install them (`pre-commit install`). GitHub Actions pipeline will run the hooks to demonstrate that the code has good quality.

I plan to make several templates with different approaches of CI. For this reason the project contains several branches, you should use the branch convenient for your purposes.

- [x] [junior branch](https://github.com/pantafive/abc-python/tree/junior) - is a basic template without Docker and other complex things. Will be convenient for beginners and small projects.

- [ ] advanced branch - will contain more complicated CI based on docker-compose.


## Quick start

### "junior" branch

1. [Install poetry](https://python-poetry.org/docs/#installation).

   > You can adopt the code to use pip, but it may be quite difficult, 
   > so I recommend taking a look at Poetry - you will love it.

2. [Install pre-commit](https://pre-commit.com/#installation).

3. Fork the project

4. Clone it and checkout to certain branch (`git checkout junior`)

5. Prepare environment (`poetry install`)

6. Setup pre-commit hooks (`pre-commit install`)

7. If you use PyCharm mark `./app` directory as "Source Root".

8. Check that everything works:

    ```sh
    PYTHONPATH=./app poetry run pytest ./tests/  # test
    pre-commit run -a  # lint
    ```

9. Brake tests and push code to GiHub. CI should fail.

10. Make tests pass and commit changes.

11. Try to brake the code (e.g. remove type annotations) then try to commit them, pre-commit should protect you.

12. Enforce to commit broken code (`git commit -m "brake the code"  --no-verify`) and push it to GitHub.

13. GitHub Actions should fail, and that's the goal.

Now you should understand how everything works. Just adapt you project according to that template.

---

Feel free to fork and contribute!
