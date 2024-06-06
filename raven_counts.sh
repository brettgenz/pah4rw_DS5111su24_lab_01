echo "--raven_counts--"
echo "Number of lines with raven: $(cat pg17192.txt | grep raven | wc -l)"
echo "Number of lines with Raven: $(cat pg17192.txt | grep Raven | wc -l)"
echo "Number of lines with raven (case insensitive): $(cat pg17192.txt | grep -i raven | wc -l)"
