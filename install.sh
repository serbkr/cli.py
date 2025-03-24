#!/bin/bash


# Install the CLI app
install() {
    echo "Installing the CLI app..."
    pip3 install -e .
}


# Uninstall the CLI app
uninstall() {
    echo "Uninstalling the CLI app..."
    pip3 uninstall -y your_package_name  # Replace with your actual package name
}


# Check the command line argument
if [ "$1" == "install" ]; then
    install
elif [ "$1" == "uninstall" ]; then
    uninstall
else
    echo "Usage: $0 {install|uninstall}"
fi
