FROM manimcommunity/manim:latest

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    apt-utils \
    ffmpeg \
    git \
    texlive-lang-japanese \
    texlive-lang-english \
    texlive-luatex \
    texlive-latex-recommended \
    texlive-latex-extra \
    fonts-lmodern \
    texlive-xetex \
    latex-cjk-common \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-extra-utils \
    latexmk \
    liblog-log4perl-perl \
    libyaml-tiny-perl \
    libfile-homedir-perl \
    liblog-dispatch-perl \
    fonts-ipafont \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && tlmgr install zxjatype

USER ${USER}

CMD [ "/bin/bash" ]