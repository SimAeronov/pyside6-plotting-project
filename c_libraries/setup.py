from distutils.core import setup, Extension
def main():
    # Uncomment to debug: run with -v > output.txt 2>&1
    # os.environ['DISTUTILS_DEBUG'] = '1'
    
    module = Extension("custom_math", sources=["custom_math.c"])

    setup(name="custom_math",
          version="1.0.0",
          description="Simonko's custom implementation of Simpsons rule for integration",
          author="Simonko",
          ext_modules=[module],
          script_args=["build_ext", "--compiler=mingw32"],
          )

if __name__ == "__main__":
    main()