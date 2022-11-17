func f() -> (res: felt):
  return (res=12)
end

func main() -> ():
  let (fres) = f()
  assert fres = 12
  return ()
end
