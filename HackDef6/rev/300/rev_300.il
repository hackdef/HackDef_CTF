.method public hidebysig static void  connect_to_c2() cil managed
{
  // Code size       360 (0x168)
  .maxstack  5
  .locals init ([0] string[] data,
           [1] char und,
           [2] int32 di,
           [3] string qu,
           [4] char am,
           [5] string t,
           [6] string 'il',
           [7] uint8[] base64EncodedBytes,
           [8] string IL,
           [9] string chi,
           [10] string[] ars,
           [11] string flag)
  IL_0000:  nop
  IL_0001:  ldstr      "Funcion que se conecta al C2 para exfiltrar datos"
  IL_0006:  call       void [mscorlib]System.Console::WriteLine(string)
  IL_000b:  nop
  IL_000c:  ldstr      "Preparando datos para exfiltrar..."
  IL_0011:  call       void [mscorlib]System.Console::WriteLine(string)
  IL_0016:  nop
  IL_0017:  ldc.i4.5
  IL_0018:  newarr     [mscorlib]System.String
  IL_001d:  dup
  IL_001e:  ldc.i4.0
  IL_001f:  ldstr      "hackdef{"
  IL_0024:  stelem.ref
  IL_0025:  dup
  IL_0026:  ldc.i4.1
  IL_0027:  ldstr      "_0f_"
  IL_002c:  stelem.ref
  IL_002d:  dup
  IL_002e:  ldc.i4.2
  IL_002f:  ldstr      "!}"
  IL_0034:  stelem.ref
  IL_0035:  dup
  IL_0036:  ldc.i4.3
  IL_0037:  ldstr      "_g00D_"
  IL_003c:  stelem.ref
  IL_003d:  dup
  IL_003e:  ldc.i4.4
  IL_003f:  ldstr      "nd1ng"
  IL_0044:  stelem.ref
  IL_0045:  stloc.0
  IL_0046:  ldc.i4.s   95
  IL_0048:  call       char [mscorlib]System.Convert::ToChar(int32)
  IL_004d:  stloc.1
  IL_004e:  ldc.i4.s   10
  IL_0050:  stloc.2
  IL_0051:  ldloc.2
  IL_0052:  ldc.i4.s   -6
  IL_0054:  call       string rev_300.Program::suma(int32,
                                                    int32)
  IL_0059:  stloc.3
  IL_005a:  ldc.i4.s   65
  IL_005c:  call       char [mscorlib]System.Convert::ToChar(int32)
  IL_0061:  stloc.s    am
  IL_0063:  ldc.i4.2
  IL_0064:  ldc.i4.1
  IL_0065:  call       string rev_300.Program::suma(int32,
                                                    int32)
  IL_006a:  stloc.s    t
  IL_006c:  ldstr      "SUxDT0RF"
  IL_0071:  stloc.s    'il'
  IL_0073:  ldloc.s    'il'
  IL_0075:  call       uint8[] [mscorlib]System.Convert::FromBase64String(string)
  IL_007a:  stloc.s    base64EncodedBytes
  IL_007c:  call       class [mscorlib]System.Text.Encoding [mscorlib]System.Text.Encoding::get_UTF8()
  IL_0081:  ldloc.s    base64EncodedBytes
  IL_0083:  callvirt   instance string [mscorlib]System.Text.Encoding::GetString(uint8[])
  IL_0088:  stloc.s    IL
  IL_008a:  ldc.i4.4
  IL_008b:  ldc.i4.1
  IL_008c:  call       string rev_300.Program::suma(int32,
                                                    int32)
  IL_0091:  stloc.s    chi
  IL_0093:  ldc.i4.5
  IL_0094:  newarr     [mscorlib]System.String
  IL_0099:  dup
  IL_009a:  ldc.i4.0
  IL_009b:  ldstr      "h"
  IL_00a0:  stelem.ref
  IL_00a1:  dup
  IL_00a2:  ldc.i4.1
  IL_00a3:  ldstr      "r"
  IL_00a8:  stelem.ref
  IL_00a9:  dup
  IL_00aa:  ldc.i4.2
  IL_00ab:  ldstr      "t"
  IL_00b0:  stelem.ref
  IL_00b1:  dup
  IL_00b2:  ldc.i4.3
  IL_00b3:  ldstr      "u"
  IL_00b8:  stelem.ref
  IL_00b9:  dup
  IL_00ba:  ldc.i4.4
  IL_00bb:  ldstr      "v"
  IL_00c0:  stelem.ref
  IL_00c1:  stloc.s    ars
  IL_00c3:  ldc.i4.s   20
  IL_00c5:  newarr     [mscorlib]System.String
  IL_00ca:  dup
  IL_00cb:  ldc.i4.0
  IL_00cc:  ldloc.0
  IL_00cd:  ldc.i4.0
  IL_00ce:  ldelem.ref
  IL_00cf:  stelem.ref
  IL_00d0:  dup
  IL_00d1:  ldc.i4.1
  IL_00d2:  ldloc.s    ars
  IL_00d4:  ldc.i4.3
  IL_00d5:  ldelem.ref
  IL_00d6:  stelem.ref
  IL_00d7:  dup
  IL_00d8:  ldc.i4.2
  IL_00d9:  ldloca.s   und
  IL_00db:  call       instance string [mscorlib]System.Char::ToString()
  IL_00e0:  stelem.ref
  IL_00e1:  dup
  IL_00e2:  ldc.i4.3
  IL_00e3:  ldloc.s    ars
  IL_00e5:  ldc.i4.0
  IL_00e6:  ldelem.ref
  IL_00e7:  stelem.ref
  IL_00e8:  dup
  IL_00e9:  ldc.i4.4
  IL_00ea:  ldloc.3
  IL_00eb:  stelem.ref
  IL_00ec:  dup
  IL_00ed:  ldc.i4.5
  IL_00ee:  ldloc.s    ars
  IL_00f0:  ldc.i4.4
  IL_00f1:  ldelem.ref
  IL_00f2:  stelem.ref
  IL_00f3:  dup
  IL_00f4:  ldc.i4.6
  IL_00f5:  ldloc.s    t
  IL_00f7:  stelem.ref
  IL_00f8:  dup
  IL_00f9:  ldc.i4.7
  IL_00fa:  ldloca.s   und
  IL_00fc:  call       instance string [mscorlib]System.Char::ToString()
  IL_0101:  stelem.ref
  IL_0102:  dup
  IL_0103:  ldc.i4.8
  IL_0104:  ldloca.s   am
  IL_0106:  call       instance string [mscorlib]System.Char::ToString()
  IL_010b:  stelem.ref
  IL_010c:  dup
  IL_010d:  ldc.i4.s   9
  IL_010f:  ldloc.0
  IL_0110:  ldc.i4.3
  IL_0111:  ldelem.ref
  IL_0112:  stelem.ref
  IL_0113:  dup
  IL_0114:  ldc.i4.s   10
  IL_0116:  ldstr      "und"
  IL_011b:  stelem.ref
  IL_011c:  dup
  IL_011d:  ldc.i4.s   11
  IL_011f:  ldloc.s    t
  IL_0121:  stelem.ref
  IL_0122:  dup
  IL_0123:  ldc.i4.s   12
  IL_0125:  ldloc.s    ars
  IL_0127:  ldc.i4.1
  IL_0128:  ldelem.ref
  IL_0129:  stelem.ref
  IL_012a:  dup
  IL_012b:  ldc.i4.s   13
  IL_012d:  ldloc.s    chi
  IL_012f:  stelem.ref
  IL_0130:  dup
  IL_0131:  ldc.i4.s   14
  IL_0133:  ldloc.s    ars
  IL_0135:  ldc.i4.2
  IL_0136:  ldelem.ref
  IL_0137:  stelem.ref
  IL_0138:  dup
  IL_0139:  ldc.i4.s   15
  IL_013b:  ldloc.3
  IL_013c:  stelem.ref
  IL_013d:  dup
  IL_013e:  ldc.i4.s   16
  IL_0140:  ldloc.0
  IL_0141:  ldc.i4.4
  IL_0142:  ldelem.ref
  IL_0143:  stelem.ref
  IL_0144:  dup
  IL_0145:  ldc.i4.s   17
  IL_0147:  ldloc.0
  IL_0148:  ldc.i4.1
  IL_0149:  ldelem.ref
  IL_014a:  stelem.ref
  IL_014b:  dup
  IL_014c:  ldc.i4.s   18
  IL_014e:  ldloc.s    IL
  IL_0150:  stelem.ref
  IL_0151:  dup
  IL_0152:  ldc.i4.s   19
  IL_0154:  ldloc.0
  IL_0155:  ldc.i4.2
  IL_0156:  ldelem.ref
  IL_0157:  stelem.ref
  IL_0158:  call       string [mscorlib]System.String::Concat(string[])
  IL_015d:  stloc.s    flag
  IL_015f:  ldloc.s    flag
  IL_0161:  call       void [mscorlib]System.Console::WriteLine(string)
  IL_0166:  nop
  IL_0167:  ret
} // end of method Program::connect_to_c2

