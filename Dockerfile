FROM python:3.14
WORKDIR /hospital
COPY patient_reg.py .
CMD ["python", "patient_reg.py"]
