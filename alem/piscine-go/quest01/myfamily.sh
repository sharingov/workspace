curl https://01.alem.school/assets/superhero/all.json | jq '.[] | select(.id=='$HERO_ID')' | jq '.connections.relatives' | sed 's/^.//' | sed 's/.$//'
