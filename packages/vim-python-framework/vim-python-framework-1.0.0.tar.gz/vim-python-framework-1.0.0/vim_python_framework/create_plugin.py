import os
import sys
sys.path.append('./myplugin')
import vim_python_framework as my_framework

def create_plugin(plugin_name):
    base_path = os.path.join(os.getcwd(), plugin_name)
    include_path = os.path.join(base_path, 'include')
    src_path = os.path.join(base_path, 'src')
    plugin_path = os.path.join(base_path, 'plugin')
    vim_script_path = my_framework.get_vim_framework_file()

    os.makedirs(include_path, exist_ok=True)
    os.makedirs(src_path, exist_ok=True)
    os.makedirs(plugin_path, exist_ok=True)

    with open(os.path.join(plugin_path, 'framework.vim') , 'w') as f:
        f.write("""
let current_dir = expand('<sfile>:p:h/')
let g:include_path = resolve(current_dir . '/' . '../include')
let current_dir = expand('<sfile>:p:h/')
let g:src_path = resolve(current_dir . '/' . '../src')

python3 << EOF
import sys

sys.path.append(vim.eval('g:include_path'))
sys.path.append(vim.eval('g:src_path'))
EOF
                """)
        f.write("\nsource " + vim_script_path)

    with open(os.path.join(include_path, 'hello.py') , 'w') as f:
        f.write("""
import vim

def world():
    # Emulate text write using vim python module
    vim.command("normal! i>>  ")
    vim.command("normal! iHello world!")

    return "This is a sample output returned"
                """)

    print(f'Created plugin "{plugin_name}" in "{base_path}".')

def main():
    if len(sys.argv) != 2:
        print('Usage: create-vim-python-plugin <plugin_name>')
        sys.exit(1)

    plugin_name = sys.argv[1]
    create_plugin(plugin_name)

if __name__ == '__main__':
    main()
