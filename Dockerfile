FROM alpine:3.9

# Update
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# Install dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY sudoku /sudoku
COPY model /model

# Get the model

EXPOSE 5000
CMD ["python", "sudoku/app.py"]
