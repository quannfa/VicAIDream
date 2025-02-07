#%% init project env
import EsyPro
sfs = EsyPro.ScriptResultManager('zqf',locals(), version=0)

def output_env():
    pre_fix = sfs.package_path.cat('.condaenv')
    import os
    os.system(
        f"conda env export > environment.yml"
    )


#%% main
if __name__ == '__main__':
    print(f'start {__file__}')

    output_env()
    
    #%% end script
    print(f'end {__file__}')
