

from datetime import datetime, timedelta


class CheckDateGaps:

    @staticmethod
    def check_date_gaps(date_list):
        """
        Check for date gaps in a list of date strings.

        Args:
            date_list (list): A list of date strings in the format '%Y-%m-%d'.

        Returns:
            list: A list of missing dates (as strings) that have gaps between them.

        Examples:
            >>> dates = ['2023-05-01', '2023-05-02', '2023-05-04', '2023-05-07']
            >>> check_date_gaps(dates)
            ['2023-05-03', '2023-05-05', '2023-05-06']

            >>> dates = ['2023-01-01', '2023-01-03', '2023-01-05']
            >>> check_date_gaps(dates)
            ['2023-01-02', '2023-01-04']

            >>> dates = ['2023-12-31']
            >>> check_date_gaps(dates)
            []

        """

        # Convert date strings to datetime objects
        dates = [datetime.strptime(date_str, '%Y-%m-%d') if isinstance(date_str, str) else date_str for date_str in
                 date_list if isinstance(date_str, str) or isinstance(date_str, datetime)]

        # dates = [datetime.strptime(date_str, '%Y-%m-%d') for date_str in date_list if isinstance(date_str, str)]
        #
        # for date_str in date_list:
        #     if isinstance(date_str, str):
        #         dates.append(datetime.strptime(date_str, '%Y-%m-%d'))
        #     elif isinstance(date_str, datetime):
        #         dates.append(date_str)

        # Sort the datetime objects
        dates.sort()

        # Check for gaps
        gaps = []
        for i in range(len(dates) - 1):
            if dates[i + 1] - dates[i] > timedelta(days=1):
                missing_date = dates[i] + timedelta(days=1)
                while missing_date < dates[i + 1]:
                    gaps.append(missing_date.strftime('%Y-%m-%d'))
                    missing_date += timedelta(days=1)

        return gaps


