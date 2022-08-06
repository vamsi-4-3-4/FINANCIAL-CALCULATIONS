const ending_retained_earnings=(beginning_retained_earnings,net_income,dividens)=>{
    return beginning_retained_earnings+net_income-dividens
}
var beginning_retained_earnings=99
var net_income=33
var dividens=3.0
var endingretainedearnings=ending_retained_earnings(beginning_retained_earnings,net_income,dividens)
console.log(endingretainedearnings)
