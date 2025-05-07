# For Nix Environment Selector extension
(builtins.getFlake ("git+file://" + toString ./.)).devShells.${builtins.currentSystem}.default