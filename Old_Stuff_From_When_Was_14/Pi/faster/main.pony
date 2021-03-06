use "lib:m"
use "format"

actor Calculate
  let pi: F64 = 3.14159265358979323846264338327950

actor Main
  new create(env: Env) =>
    let numberSides: U32 = 414327
    let actors: U32 = 4
    var calculatedPi: F32 = 0
    var count: U32 = 0
    repeat
      count = count + 1
      calculatedPi = calculateTheThingForXSides(numberSides)
    until count > numberSides end
    env.out.print(disp("Calculation", calculatedPi.f64()))
    env.out.print(disp("Count", count.f64()))
    let num: F64 = ((5*3.14159265)/180.0)
    env.out.print(tan(num).string())
  fun disp(desc: String, v: F64, fmt: FormatFloat = FormatDefault): String =>
    Format(desc where width = 15)
      + ":"
      + Format.float[F64](v where width = 10, align = AlignRight, fmt = fmt, prec = 20)
  fun calculateTheThingForXSides(sides: U32): F32 =>
    let apothem: F32 = calculateApothem(sides)
    sides.f32() / (apothem * 2)
  fun tan(x: F64): F64 =>
    @tan[F64](x)
  fun radians(x: F64): F64 =>
    let pi: F64 = 3.14159265358979323846264338327950
    (x*pi)/180
  fun calculateApothem(sides: U32): F32 =>
    (1.0 / ( tan(radians(180.0 / sides.f64()) )  * 2 )).f32()
