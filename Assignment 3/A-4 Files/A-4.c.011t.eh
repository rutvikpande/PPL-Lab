
;; Function main (main, funcdef_no=0, decl_uid=1910, cgraph_uid=1, symbol_order=0)

main ()
{
  int * p;
  int i;
  int b[3];
  int a[3];
  int D.1920;

  b[0] = 1;
  b[1] = 2;
  b[2] = 3;
  i = 0;
  goto <D.1917>;
  <D.1916>:
  _1 = b[i];
  a[i] = _1;
  i = i + 1;
  <D.1917>:
  if (i <= 2) goto <D.1916>; else goto <D.1918>;
  <D.1918>:
  p = &a;
  _2 = p + 8;
  *_2 = 5;
  a = {CLOBBER};
  b = {CLOBBER};
  D.1920 = 0;
  goto <D.1921>;
  <D.1921>:
  return D.1920;
}


