
#!/bin/bash
set -e

read -p "Want to install conda env named 'alea-carta-est'? (y/n)" answer
if [ "$answer" = "y" ]; then
  echo "Installing conda env..."
  conda create -n alea-carta-est python=3.11 -y
  source $(conda info --base)/etc/profile.d/conda.sh
  conda activate alea-carta-est
  echo "Installing requirements..."
  pip install -r requirements-developer.txt
  python3 -m ipykernel install --user --name=alea-carta-est
  conda install -c conda-forge --name alea-carta-est notebook -y
  echo "Installing pre-commit..."
  make install_precommit
  echo "Installation complete!"
  echo "Run the following command to activate the conda env: 'conda activate alea-carta-est'";
else
  echo "Installation of conda env aborted!";
fi
