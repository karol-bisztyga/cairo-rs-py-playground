%lang starknet

func f() -> (res: felt) {
  return (res=12);
}

@view
func main() -> () {
  let (fres) = f();
  assert fres = 12;
  return ();
}