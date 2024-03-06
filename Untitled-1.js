// Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQAetawTHfGHdLZiJWhMri79kP-_kLxgvYBe8bE75X3HspK1KRnwK_-JbP156GtxZo_e2wsukB9Kl1IZ3Jzvp7NcheOCo0tWayobVmP-qhs8EfkIPSDBoklOHQsmADbiw_Tj-Ni3QCc2CyH-S2SyaBbsj0lqjuXfVs6YkH25yZJLLwCTQ5K0iTIDPC-1mx6lkRVh4e4Wfy9w_RVqmRo2quUlqX3BmzG3pEGJMsoAo-rQTZbiMUOEt9qr06USegg38vB7xilsNgdjBFSo7bEp7ymY';
async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body:JSON.stringify(body)
  });
  return await res.json();
}

const topTracksIds = [
  '0F8f3H1eWDaWsfoLKGnoHv','6jmf4OxSGzdgthZruXtcqu','59aL2q2UPYJkgLTSv0WTlB','6QFQqqYye5lAcnhCALvxKJ','0kEZlJh4mK1QRfb3CT5LPk'
];

async function getRecommendations(){
  // Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-recommendations
  return (await fetchWebApi(
    `v1/recommendations?limit=5&seed_tracks=${topTracksIds.join(',')}`, 'GET'
  )).tracks;
}

const recommendedTracks = await getRecommendations();
console.log(
  recommendedTracks.map(
    ({name, artists}) =>
      `${name} by ${artists.map(artist => artist.name).join(', ')}`
  )
);