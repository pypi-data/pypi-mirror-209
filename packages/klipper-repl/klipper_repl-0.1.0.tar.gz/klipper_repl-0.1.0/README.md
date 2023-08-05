# klipper-repl

_The missing Klipper command line._

`klipper-repl` is a command line reimplementation of the browser-based G-Code
console implemented by Klipper frontends like [Fluidd](https://docs.fluidd.xyz/)
and [Mainsail](https://docs.mainsail.xyz/). Its features include:
- Automatic reconnection if Klipper restarts or is unavailable
- Scripting support
- Multiple G-Code commands per line -- use `,` as a separator
- Syntax highlighting for both G-Code and user-defined macros
- Tab autocompletion for user-defined macros
- M112 emergency stop processing
- Support for multiple printers via [GNU
  Parallel](https://www.gnu.org/software/parallel/)

## Installing
### Via a Nix flake
If you have the [Nix package manager](https://nixos.org/), this package is
available as a [Nix flake](https://nixos.wiki/wiki/Flakes). An example
`flake.nix` for a host running Klipper is:

``` nix
{
  inputs = {
    nix-doom-emacs.url = "github:unjordy/klipper-repl";
  };

  outputs = {
    self,
    nixpkgs,
    klipper-repl,
    ...
  }: {
    nixosConfigurations.klipperHost = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [
        {
          environment.systemPackages = [
            klipper-repl.packages.${system}.default
          ];
        }
      ];
    };
  };
}
```

You can also run `klipper-repl` without installing it using

``` nix
nix run github:unjordy/klipper-repl
```

### Via pip
