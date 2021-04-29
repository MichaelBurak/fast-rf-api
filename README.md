> # [FastAPI Random Forest Iris Dataset Classifier API](https://iris-classifier-client.netlify.app/)
>
> ![Alt Text](https://i.imgur.com/Z44iCPY.png)

## Project Description

- Uses a pickled sklearn RandomForestClassifier to classify based off of user input what type of Iris from the famous [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris) the values would correspond to and outputs the result.
- Built to try out FastAPI(_I'm a fan now_), practice deploying machine learning models, Vue.js on the frontend, pytest with TravisCI(_see that neat badge?_) for basic tests with CI, and more. Generally where I'm trying out new things or brushing up on older stuff with a project-based approach by implementation.

## Up Next

- **Docker** properly set up and incorporated into deployment.
- CD added to CI through **GitHub workflows/actions**.
- **Prometheus** metrics of all things, I don't expect much traffic or anything but I want to test out traffic and the stack with **Grafana** on Heroku.
- **Better frontend**: really want to display a representative image conditionally of the classified flower, and more interactivity maybe.
- **More tests, more routes, more functionality overall**: though this is limited by the scope of the project being "classifier with a frontend" after all.
- Get the Client code up on GitHub and implement best Vue.js practices because it's a similar mess.

## Notes

- Heroku **_will coldstart_** and take a little bit to give classifications. That's just how it be, unless I pay more money, and I'm not at that point for a toy/example project.

## Citations/References/Etcs

- The [excellent testdriven.io course on FastAPI with TDD and Docker](https://testdriven.io/courses/tdd-fastapi/) is getting a lot of play in implementing the concepts here.
- [This Udemy course](https://www.udemy.com/course/deploy-data-science-nlp-models-with-docker-containers) on deploying ML models with Docker was the base of this project.
- Dua, D. and Graff, C. (2019). UCI Machine Learning Repository http://archive.ics.uci.edu/ml. Irvine, CA: University of California, School of Information and Computer Science.
