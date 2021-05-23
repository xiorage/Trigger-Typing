function FindModule(item)
{
            var req = window.webpackJsonp.push([[], {'__extra_id__': (module, exports, req) => module.exports = req}, [['__extra_id__']]]);

            for (const in1 in req.c) {
                if (req.c.hasOwnProperty(in1)) {
                    const m = req.c[in1].exports;
                    if (m && m.__esModule && m.default && m.default[item]) return m.default;
                    if (m && m[item]) return m;
                }
            }
}

let time = 86400;
let guildid = "Server-ID-Here";
let channelid = "Channel-ID-Here";

var loop = setInterval(function()
 {
