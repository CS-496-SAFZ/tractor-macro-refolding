pub unsafe extern "C" fn call_macro(
    mut x: libc::c_double,
    mut y: libc::c_double,
) -> libc::c_double {
    return x * y;
}
