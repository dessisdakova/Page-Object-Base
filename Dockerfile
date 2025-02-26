FROM python:3.9-slim
USER root

# install dependancies for Chrome and tools
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libexpat1 \
    libfontconfig1 \
    libgbm1 \
    libgcc1 \
    libgdk-pixbuf2.0-0 \
    libgl1 \
    libgraphene-1.0-0 \
    libgtk-3-0 \
    libidn2-0 \
    libjpeg62-turbo \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libstdc++6 \
    libx11-6 \
    libx11-xcb1 \
    libxcb-dri3-0 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxrender1 \
    libxss1 \
    libxtst6

# install Chrome browser
RUN wget https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.126/linux64/chrome-linux64.zip
RUN unzip chrome-linux64.zip -d /tmp/
RUN mkdir -p /opt/google/chrome/
RUN mv /tmp/chrome-linux64/* /opt/google/chrome/
RUN rmdir /tmp/chrome-linux64

# install Chrome driver and add it to PATH
RUN wget https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.126/linux64/chromedriver-linux64.zip
RUN unzip chromedriver-linux64.zip -d /tmp/
RUN mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/
RUN rm -rf /tmp/chromedriver-linux64
RUN chmod +x /usr/local/bin/chromedriver

WORKDIR /project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]