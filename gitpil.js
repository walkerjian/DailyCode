function calculateDaysBetweenDates(begin, end) { 
  const oneDay = 1000 * 60 * 60 * 24;
  const differenceMs = end.getTime() - begin.getTime();
  return Math.round(differenceMs / oneDay);
}