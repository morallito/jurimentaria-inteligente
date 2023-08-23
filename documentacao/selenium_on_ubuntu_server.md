# Selenium and python on Ubuntu server (debian distros)

## Installing selenium
```
python -m pip install selenium==4.11.2
```

## Installin chromium     
``` 
sudo apt install -y chromium-browser=116.0.5845.96
```

## Get and install chrome driver


Since we are working with the chromium-browser on the version 116.0.5845.96, we need to install the driver compatible with such version.

```
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

Now chrome driver is installed at /usr/bin/chromedriver and ready to use toguether with selenium.

