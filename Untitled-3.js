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

async function getTopTracks(){
  // Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
  return (await fetchWebApi(
    'v1/me/top/tracks?time_range=long_term&limit=5', 'GET'
  )).items;
}

const topTracks = await getTopTracks();
console.log(
  topTracks?.map(
    ({name, artists}) =>
      `${name} by ${artists.map(artist => artist.name).join(', ')}`
  )
);