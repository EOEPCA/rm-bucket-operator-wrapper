
<!-- PROJECT SHIELDS -->
<!--
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
![Build][build-shield]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/EOEPCA/rm-bucket-operator-wrapper">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">EOEPCA Bucket Operator Wrapper</h3>

  <p align="center">
    This repository includes the EOEPCA Bucket Operator Wrapper component
    <br />
    <a href="https://github.com/EOEPCA/rm-bucket-operator-wrapper"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/EOEPCA/rm-bucket-operator-wrapper">View Demo</a>
    ·
    <a href="https://github.com/EOEPCA/rm-bucket-operator-wrapper/issues">Report Bug</a>
    ·
    <a href="https://github.com/EOEPCA/rm-bucket-operator-wrapper/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Documentation](#documentation)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

## About The Project

During workspace creation the `workspace-api` needs to create an object storage bucket for the user. The method by which the bucket is created is a function of the hosting infrastructure object storage layer - i.e. there is no ‘common’ approach for the `workspace-api` to perform the bucket creation.

In order to allow this bucket creation step to be customised by the platform integrator, the `workspace-api` is configured with a webhook endpoint that is invoked to effect the bucket creation on behalf of the `workspace-api`.

The Bucket Oprator Wrapper provides an wrapper around the original Bucket Operator for creating S3 Object Storage backend for CreoDIAS.

### Built With

- FastAPI

<!-- GETTING STARTED -->

## Getting Started

### Installation

TBD

## Documentation

The component documentation can be found at https://eoepca.github.io/rm-bucket-operator-wrapper/.

<!-- USAGE EXAMPLES -->


<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/EOEPCA/rm-bucket-operator-wrapper/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the Apache-2.0 License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Project Link: [https://github.com/EOEPCA/rm-bucket-operator-wrapper](https://github.com/EOEPCA/rm-bucket-operator-wrapper)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- README.md is based on [this template](https://github.com/othneildrew/Best-README-Template) by [Othneil Drew](https://github.com/othneildrew).

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/EOEPCA/rm-bucket-operator-wrapper.svg?style=flat-square
[contributors-url]: https://github.com/EOEPCA/rm-bucket-operator-wrapper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EOEPCA/rm-bucket-operator-wrapper.svg?style=flat-square
[forks-url]: https://github.com/EOEPCA/rm-bucket-operator-wrapper/network/members
[stars-shield]: https://img.shields.io/github/stars/EOEPCA/rm-bucket-operator-wrapper.svg?style=flat-square
[stars-url]: https://github.com/EOEPCA/rm-bucket-operator-wrapper/stargazers
[issues-shield]: https://img.shields.io/github/issues/EOEPCA/rm-bucket-operator-wrapper.svg?style=flat-square
[issues-url]: https://github.com/EOEPCA/rm-bucket-operator-wrapper/issues
[license-shield]: https://img.shields.io/github/license/EOEPCA/rm-bucket-operator-wrapper.svg?style=flat-square
[license-url]: https://github.com/EOEPCA/rm-bucket-operator-wrapper/blob/master/LICENSE
[build-shield]: https://www.travis-ci.com/EOEPCA/rm-bucket-operator-wrapper.svg?branch=master

