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

const tracksUri = [
  'spotify:track:0F8f3H1eWDaWsfoLKGnoHv','spotify:track:1KVczjazCcCCgM3gXXUl47','spotify:track:6jmf4OxSGzdgthZruXtcqu','spotify:track:7ucWpsVpbeCPNIHfyf5i2w','spotify:track:59aL2q2UPYJkgLTSv0WTlB','spotify:track:0HGeLGchMkRHhMbRSCinAP','spotify:track:6QFQqqYye5lAcnhCALvxKJ','spotify:track:6Hdx6kABwuNPpGSdvkoR9j','spotify:track:0kEZlJh4mK1QRfb3CT5LPk','spotify:track:4Yt1yBsZckANMLohLeluL0'
];

async function createPlaylist(tracksUri){
  const { id: user_id } = await fetchWebApi('v1/me', 'GET')

  const playlist = await fetchWebApi(
    `v1/users/${user_id}/playlists`, 'POST', {
      "name": "My recommendation playlist",
      "description": "Playlist created by the tutorial on developer.spotify.com",
      "public": false
  })

  await fetchWebApi(
    `v1/playlists/${playlist.id}/tracks?uris=${tracksUri.join(',')}`,
    'POST'
  );

  return playlist;
}

const createdPlaylist = await createPlaylist(tracksUri);
console.log(createdPlaylist.name, createdPlaylist.id);
