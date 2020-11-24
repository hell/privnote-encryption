# privnote-encryption
A simple privnote-encryption class that can be used in any program/script in Python

A simple way to encrypt your privnote data. 

You can use example.py as an example to see how you can implement/use it. 

An example that can be used to post a new note: 

```
session.post(self.ENDPOINT + 'legacy/', data=self.format_data(self.encrypt(text)), headers={'X-Requested-With': 'XMLHttpRequest'})
```
