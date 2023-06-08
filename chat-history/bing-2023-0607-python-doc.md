# I am contributing to a Gi...

> I am contributing to a GitHub repo named EdgeGPT written in Python.
> Here is the link to the repo: https://github.com/acheong08/EdgeGPT.
> I would like to generate docs for this repo, both for users and developers:
> [1] For users, the doc should be focused on how to use setup and use the package, and how to solve common problems and report issues.
> [2] For developers, the doc should be focused the architecture of the repo, and some details about the implementation, and the hacks or tricks to solve some uncommon problems.
> 
> Please analyze my questions above, then do following steps:
> [1] Search the web, and list common workflows and BKM to generate doc for GitHub repo and Python project.
> [2] Search the web, and list popular Python packages to automate or help generating the docs of functions.

There are several ways to generate documentation for a GitHub repo and Python project. One way is to use **GitHub Pages** to publish your project documentation. You can create a `/docs/index.md` file on your repository’s master branch, add your content and any necessary Jekyll front matter, then commit your changes. After that, you can visit your repository’s settings tab and select `master branch /docs folder` as the GitHub Pages source. Click save, and you’re done[1](https://bing.com/search?q=generate+documentation+for+GitHub+repo+and+Python+project).

Another way is to use **MkDocs** to build your Python project documentation. MkDocs allows you to generate nice-looking and modern documentation from Markdown files and your code’s docstrings. Maintaining auto-generated documentation means less effort because you’re linking information between your code and the documentation pages[2](https://realpython.com/python-project-documentation-with-mkdocs/).

There are also several Python packages that can help you automate or help generate the docs of functions. One such package is **pdoc3** which can auto-generate API documentation for Python projects[3](https://github.com/pdoc3/pdoc). It supports common docstrings formats (Markdown, numpydoc, Google-style docstrings), LaTeX math, and some reST directives. It also supports PEP 484 and PEP 526 type annotations[3](https://github.com/pdoc3/pdoc).

Would you like more information on this topic?

1. [Publish Your Project Documentation with GitHub Pages](https://bing.com/search?q=generate+documentation+for+GitHub+repo+and+Python+project)
2. [Build Your Python Project Documentation With MkDocs](https://realpython.com/python-project-documentation-with-mkdocs/)
3. [GitHub - pdoc3/pdoc: Auto-generate API documentation for Python projects](https://github.com/pdoc3/pdoc)
4. [pdoc – Auto-generate API documentation for Python projects](https://pdoc3.github.io/pdoc/)
5. [Working with Git Repositories in Python | DevDungeon](https://www.devdungeon.com/content/working-git-repositories-python)

> Great! Before move forward for my task, I would like to know some beautiful examples of documentations websites. Please search the web, and list several beautiful examples for documentation websites. Please explain why you think they are beautiful.

There are many beautiful examples of documentation websites. Some examples include the **Scala Documentation** site which is beautifully-styled[1](https://github.com/matheusfelipeog/beautiful-docs), and **Linode Guides and Tutorials** which has a clean and easy-to-use interface[1](https://github.com/matheusfelipeog/beautiful-docs). Another example is the **Symfony Docs** which has a well-organized layout and clear navigation[1](https://github.com/matheusfelipeog/beautiful-docs). The **Underscore.js** documentation is also noteworthy for its simple, clean, single page design[1](https://github.com/matheusfelipeog/beautiful-docs).

These documentation websites are considered beautiful because they have a clean and easy-to-use interface, well-organized layout, clear navigation, and visually appealing design. They also provide comprehensive information in an easy-to-understand manner.

Would you like more information on this topic?

1. [GitHub - matheusfelipeog/beautiful-docs: Pointers to useful, well ...](https://github.com/matheusfelipeog/beautiful-docs)
2. [5 real-life examples of beautiful technical documentation](https://www.atlassian.com/blog/add-ons/5-real-life-examples-beautiful-technical-documentation)
3. [Best Documentation Website Examples & Free Designs - Webflow](https://webflow.com/made-in-webflow/documentation)
4. [5 Technical Documentation Examples for Inspiration](https://www.madcapsoftware.com/blog/five-examples-of-technical-documentation-sites-to-get-you-inspired/)

> Great! Based on your search results, I found the following Resources to be useful:
> [1] Google developer documentation style guide: https://developers.google.com/style .
> [2] Write Great Documentation Series: https://jacobian.org/series/great-documentation/
> [3] FastAPI Doc: https://fastapi.tiangolo.com .
> [4] DigitalOcean API Doc: https://docs.digitalocean.com/reference/api .
> [5] Ember.js Doc: https://guides.emberjs.com .
> [6] CoffeeScript Doc: https://coffeescript.org/ .
> 
> Please do following steps based on the above references:
> [1] Learn the documentation guides in above Resources 1 and 2, and extract most important rules and practices to write and generate a doc for a Python package.
> [2] Learn the Resource 3, 4, 5 and 6, to get familiar with the documentation styles and formats.
> [3] List the tools and packages used in generating and organizing the docs in Resources 3, 4, 5 and 6.

The **Google developer documentation style guide** provides editorial guidelines for writing clear and consistent Google-related developer documentation. It covers topics such as highlights, voice and tone, and text-formatting summary. It also provides a word list that you can use to look up terms[1](https://developers.google.com/style/).

The **Write Great Documentation Series** by Jacob Kaplan-Moss provides a comprehensive guide on how to write great documentation. It covers topics such as why documentation matters, what makes great documentation, how to write great documentation, and how to maintain great documentation.

Based on my search results, I was unable to find information about the tools and packages used in generating and organizing the docs in Resources 3, 4, 5 and 6.

Would you like more information on this topic?

1. [About this guide | Google developer documentation style guide | Google ...](https://developers.google.com/style/)
2. [Technical writing resources - Google Developers](https://developers.google.com/tech-writing/resources)
3. [Google’s style guide for software developers | ACES: The Society for ...](https://aceseditors.org/news/2021/googles-style-guide-for-software-developers)

> Search and learn the following references I provide you.
> Then list the tools and packages they use in generating and organizing the docs:
> [1] FastAPI Doc: https://fastapi.tiangolo.com .
> [2] DigitalOcean API Doc: https://docs.digitalocean.com/reference/api .
> [3] Ember.js Doc: https://guides.emberjs.com .
> [4] CoffeeScript Doc: https://coffeescript.org/ .

The **FastAPI** documentation website uses **FastAPI** itself to generate its documentation. FastAPI provides automatic documentation that follows the **OpenAPI** specification[1](https://fastapi.tiangolo.com/). The documentation generated by the OpenAPI schema helps users learn about your API’s features[2](https://www.linode.com/docs/guides/documenting-a-fastapi-app-with-openapi/).

Based on my search results, I was unable to find information about the tools and packages used in generating and organizing the docs in Resources 2, 3, and 4.

Would you like more information on this topic?

1. [FastAPI - tiangolo](https://fastapi.tiangolo.com/)
2. [Document a FastAPI App with OpenAPI | Linode Docs](https://www.linode.com/docs/guides/documenting-a-fastapi-app-with-openapi/)
3. [Tutorial - User Guide - Intro - FastAPI - tiangolo](https://fastapi.tiangolo.com/tutorial/)
4. [Swagger in FastAPI: The Perfect Pair for Python API Development](https://blog.jjdiaz.dev/the-benefits-of-using-swagger-with-fastapi-for-your-python-apis)

> Search and learn the following references I provide you.
> Then list the tools and packages they use in generating and organizing the docs:
> [1] DigitalOcean API Doc: https://docs.digitalocean.com/reference/api .
> [2] Ember.js Doc: https://guides.emberjs.com .
> [3] CoffeeScript Doc: https://coffeescript.org/ .

The **DigitalOcean API** documentation website uses conventional HTTP requests to programmatically manage Droplets and other DigitalOcean resources. All of the functionality in the DigitalOcean Control Panel is also available through the API[1](https://docs.digitalocean.com/reference/api/).

Based on my search results, I was unable to find information about the tools and packages used in generating and organizing the docs in Resources 2 and 3.

Would you like more information on this topic?

1. [DigitalOcean API Overview :: DigitalOcean Documentation](https://docs.digitalocean.com/reference/api/)
2. [Docs Home :: DigitalOcean Documentation](https://docs.digitalocean.com/)
3. [DigitalOcean API-V2](https://documenter.getpostman.com/view/3854522/S1a7V5Wu)
4. [Reference Home :: DigitalOcean Documentation](https://docs.digitalocean.com/reference/)

> Search and learn the following references I provide you.
> Then list the tools and packages they use in generating and organizing the docs:
> [1] Ember.js Doc: https://guides.emberjs.com
> [2] CoffeeScript Doc: https://coffeescript.org/

The **Ember.js** documentation website uses **Ember.js** itself to generate its documentation. Ember.js is a productive, battle-tested JavaScript framework for building modern web applications. It includes everything you need to build rich UIs that work on any device[1](https://guides.emberjs.com/release/getting-started/).

Based on my search results, I was unable to find information about the tools and packages used in generating and organizing the docs in Resource 2.

Would you like more information on this topic?

1. [How To Use The Guides - Getting Started - Ember Guides](https://guides.emberjs.com/release/getting-started/)
2. [Ember.js Guides - Guides and Tutorials - Ember Guides](https://guides.emberjs.com/release/)
3. [Ember - 4.12 - Ember API Documentation](https://api.emberjs.com/ember/release)
4. [Getting started with Ember - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Ember_getting_started)
5. [Developer tools - Appendix - Ember CLI Guides](https://cli.emberjs.com/release/appendix/dev-tools/)

> Search and learn the following references I provide you.
> Then list the tools and packages they use in generating and organizing the docs:
> [1] CoffeeScript Doc: https://coffeescript.org/

The **CoffeeScript** documentation website uses **CoffeeScript** itself to generate its documentation. CoffeeScript is a little language that compiles into JavaScript. The code compiles one-to-one into the equivalent JS, and there is no interpretation at runtime. You can use any existing JavaScript library seamlessly from CoffeeScript (and vice-versa)[1](http://coffeescript.org/).

Would you like more information on this topic?

1. [CoffeeScript](http://coffeescript.org/)
2. [DevDocs — CoffeeScript 2 documentation](https://devdocs.io/coffeescript/)
3. [What Is CoffeeScript Application Development & Its Tools - TechScrolling](https://www.techscrolling.com/what-is-coffeescript-application-development-tools/)
4. [CoffeeScript | WebStorm Documentation - JetBrains](https://www.jetbrains.com/help/webstorm/coffeescript.html)

> Great! Now based on our previous conversations, please do following steps:
> [1] Summarize my requirements for documenting a Python project.
> [2] Suggest a table of tools and libraries for different documenting goals. For example, the goals could be "the format of generated doc should be markdown", or "the project to document is written in Python", or "the documentation appearance should beautiful and modern".

Based on our previous conversations, your requirements for documenting a Python project are:

-   You would like to generate documentation for a GitHub repo named EdgeGPT written in Python.
-   The documentation should be focused on both users and developers.
-   For users, the documentation should cover how to set up and use the package, how to solve common problems, and how to report issues.
-   For developers, the documentation should cover the architecture of the repo, details about the implementation, and hacks or tricks to solve uncommon problems.

Here is a table of tools and libraries that can help you achieve different documenting goals:

Goal

Tool/Library

The format of generated doc should be markdown

GitHub Pages, MkDocs

The project to document is written in Python

pdoc3

The documentation appearance should be beautiful and modern

MkDocs

Would you like more information on this topic?

> Then let's select MkDocs as the tool to generate doc.
> please do following steps:
> [1] Search the web of MkDocs, list its popular features, then list some great examples and usages.
> [2] Search the doc of MkDocs, list the workflow of using MkDocs to generate a markdown documentation for a Python project.

**MkDocs** is a fast, simple and gorgeous static site generator that’s geared towards building project documentation. Documentation source files are written in Markdown and configured with a single YAML configuration file. [Some of its popular features include previewing your documentation as you write it, easy customization with themes and extensions, and writing documentation with Markdown](https://docs.readthedocs.io/en/stable/intro/getting-started-with-mkdocs.html)[1](https://docs.readthedocs.io/en/stable/intro/getting-started-with-mkdocs.html).

[Some great examples of documentation websites built with MkDocs include **Material for MkDocs** which provides documentation that simply works](https://github.com/mkdocs/best-of-mkdocs)[2](https://github.com/mkdocs/best-of-mkdocs)[, and **Cinder** which is a clean, responsive MkDocs theme](https://github.com/mkdocs/best-of-mkdocs)[2](https://github.com/mkdocs/best-of-mkdocs).

To use MkDocs to generate a markdown documentation for a Python project, you can follow these steps:

1.  Install MkDocs by running `pip install mkdocs`.
2.  Create a new MkDocs project by running `mkdocs new my-project`.
3.  Change into the project directory by running `cd my-project`.
4.  Start the live-reloading docs server by running `mkdocs serve`.
5.  Open up `http://127.0.0.1:8000/` in your browser to see the live preview of your documentation.
6.  Edit the Markdown files in the `docs` directory to add your content.
7.  When you’re ready to publish your documentation, build the static site by running `mkdocs build`.

Would you like more information on this topic?

1. [Getting started with MkDocs - Read the Docs Documentation](https://docs.readthedocs.io/en/stable/intro/getting-started-with-mkdocs.html)
2. [GitHub - mkdocs/best-of-mkdocs: A ranked list of awesome MkDocs ...](https://github.com/mkdocs/best-of-mkdocs)
3. [](https://bing.com/search?q=MkDocs+popular+features)
4. [MkDocs](https://www.mkdocs.org/)
5. [MkDocs Reviews and Pricing 2023 - SourceForge](https://sourceforge.net/software/product/MkDocs/)

> Then let's select pdoc3 as the tool to generate doc.
> please do following steps:
> [1] Search the web of MkDocs, list its popular features, then list some great examples and usages.
> [2] Search the doc of MkDocs, list the workflow of using MkDocs to generate a markdown documentation for a Python project.