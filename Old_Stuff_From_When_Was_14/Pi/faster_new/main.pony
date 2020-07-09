use "lib:m"
use "format"


actor Calculate
  let pi: F64 = 3.14159265358979323846264338327950

actor Main

  fun disp(desc: String, v: F64, fmt: FormatFloat = FormatDefault): String =>
    Format(desc where width = 15)
      + ":"
      + Format.float[F64](v where width = 10, align = AlignRight, fmt = fmt, prec = 20)

  new create(env: Env) =>
    (let actors, let sides) = (env.args(1)?.u32(), env.args(2)?.u32())
    let division: F64 = sides / actors

    
