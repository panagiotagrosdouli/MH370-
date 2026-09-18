# BFO pre-end-of-flight validation target — 2026-09-18

Primary Inmarsat Table 9 supplies an unusually useful validation path because it decomposes predicted BFO into aircraft uplink Doppler, satellite uplink Doppler, downlink Doppler, AES compensation, combined satellite/AFC correction, and fixed bias.

For the stable southbound segment, the published example is:

time, lat, lon, track_deg, speed_kph, predicted_bfo_hz, measured_bfo_hz, residual_measured_minus_predicted_hz
19:41:03,0.0,93.7,186,800,108,111,3
20:41:05,-7.5,92.9,182,829,143,141,-2
21:41:27,-15.0,92.7,180,829,170,168,-2
22:41:22,-22.5,92.9,179,829,203,204,1
23:14:00,-26.6,93.0,179,829,222,217,-5
00:11:00,-33.7,93.0,180,829,252,252,0
00:19:29,-34.7,93.0,180,829,256,182,-74

The 19:41–00:11 residual RMS is sqrt((9+4+4+1+25+0)/6) = 2.68 Hz. This is the implementation acceptance target: our independent BFO forward model must reproduce the pre-EOF segment at approximately this scale before the 00:19 residual is interpreted.

DSTG Eq. 5.6 confirms the required structure:
BFO = uplink Doppler + downlink Doppler + aircraft compensation + satellite translation term + GES AFC term + bias.

Important: matching Table 9 is a code/physics validation against one illustrative trajectory, not evidence that MH370 flew exactly that path. The final -74 Hz residual is then an EOF vertical-motion constraint conditional on the horizontal trajectory model.

Status: PRIMARY_BFO_VALIDATION_VECTOR_RECOVERED / TARGET_RMS_2.68_HZ / FORWARD_MODEL_IMPLEMENTATION_NEXT.
