from camel_case_string.camel_case_string import screaming_case_string

def write_file(path, name, content, ending=".py"):
	with open(f"{path}/{name}{ending}", "w+") as f:
		f.write(content)
	f.closed

def set_settings(path):
	actions = [{'name': 'launch', 'content': """{
	// Use IntelliSense to learn about possible attributes.
	// Hover to view descriptions of existing attributes.
	// For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
	"version": "0.2.0",
	"configurations": [
		{
			"name": "Python: Current File",
			"type": "python",
			"request": "launch",
			"program": "${file}",
			"console": "integratedTerminal"
		}
	]
}"""}, {'name': 'settings', 'content': """{
	"python.testing.unittestArgs": [
		"-v",
		"-s",
		".",
		"-p",
		"test_*.py"
	],
	"python.testing.pytestEnabled": false,
	"python.testing.unittestEnabled": true
}"""}]
	for action in actions:
		write_file(f"{path}/.vscode", action['name'], action['content'], '.json')



def make(path, name):
	actions = [
		{
			"path": f"{path}", "name": f"test_{name}", 
			"content": f"""import unittest
from main import {name} 

class Test{screaming_case_string(name)}(unittest.TestCase):
	def test_{name}(self):
		self.assertEqual({name}.{name}(), 0, "Should be 0")
if __name__ == '__main__':
    unittest.main()"""
}, 
		{
			"path": f"{path}/main",  
			"name": "__init__.py", 
			"content": f"""__all__=["{name}"]"""
		},
		{ 
			"path": f"{path}/main",
			"name": f"{name}",
			"content": f"""def {name}():
	return 0

		"""	
		}
	]

	for action in actions:
		write_file(action['path'], action['name'], action['content'])


