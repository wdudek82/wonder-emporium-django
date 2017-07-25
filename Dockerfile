FROM python:3.6

EXPOSE 8000

WORKDIR /usr/src/wonder-emporium

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application's code
COPY . /usr/src/wonder-emporium

# Run the app
CMD ["/usr/src/wonder-emporium/run_app.sh"]
