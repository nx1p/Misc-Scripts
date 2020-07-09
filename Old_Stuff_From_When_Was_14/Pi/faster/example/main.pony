use "format"

actor Main
  fun disp(desc: String, v: F64, fmt: FormatFloat = FormatDefault): String =>
    Format(desc where width = 10)
      + ":"
      + Format.float[F64](v where width = 10, align = AlignRight, fmt = fmt, prec = 20)

  new create(env: Env) =>
    try
      (let x, let y) = (env.args(1)?.f64(), env.args(2)?.f64())
      env.out.print(disp("x", x))
      env.out.print(disp("y", y))
      env.out.print(disp("x * y", x * y))
    else
      let exe = try env.args(0)? else "fmt_example" end
      env.err.print("Usage: " + exe + " NUMBER1 NUMBER2")
    end
