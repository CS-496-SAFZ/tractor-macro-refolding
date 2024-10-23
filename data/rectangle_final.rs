macro_rules! multiply {
    ($x:expr, $y:expr) => {
        ($x as libc::c_double) * ($y as libc::c_double)
    };
}

pub unsafe extern "C" fn call_macro(
    mut x: libc::c_double,
    mut y: libc::c_double,
) -> libc::c_double {
    return multiply!(x, y);
}
