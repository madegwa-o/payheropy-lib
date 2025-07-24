# 💸 payheropy

A lightweight Python library for integrating with the PayHero payment gateway.

## 🚀 Features

- Simple interface to initiate mobile payments
- Easy to integrate into any Python backend
- Clean and testable code

## 📦 Dev SETUP

```bash
pip install setuptools wheel twine
python setup.py sdist bdist_wheel
twine upload dist/*

```

## 📦 Installation
```bash
pip install payheropy
```

## 🛠️ Usage

```python
from payheropy import initiate_payment

response = initiate_payment("254712345678", 250)
print(response)
```

## 🧪 Running Tests

```bash
python -m unittest discover tests
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## 📄 License

MIT © Oscar Madegwa
# payheropy-lib
