# not all entry points are listed below
@ cdecl Movie_GetAuthor(ptr)
@ cdecl Movie_GetColourDepth(ptr)
@ cdecl Movie_GetCopyright(ptr)
@ cdecl Movie_GetCurrentAudioChunk(ptr)
@ cdecl Movie_GetCurrentFrame(ptr)
@ cdecl Movie_GetCurrentVideoChunk(ptr)
@ cdecl Movie_GetFormat(ptr)
@ cdecl Movie_GetFrameRate(ptr)
@ cdecl Movie_GetFramesInBuffer(ptr)
@ cdecl Movie_GetFramesPerChunk(ptr)
@ cdecl Movie_GetMovieChunks(ptr)
@ cdecl Movie_GetName(ptr)
@ cdecl Movie_GetSoundChannels(ptr)
@ cdecl Movie_GetSoundFormatString(ptr)
@ cdecl Movie_GetSoundPrecision(ptr)
@ cdecl Movie_GetSoundRate(ptr)
@ cdecl Movie_GetSyncAdjust(ptr)
@ cdecl Movie_GetTotalFrames(ptr)
@ cdecl Movie_GetTotalTime(ptr)
@ cdecl Movie_GetXSize(ptr)
@ cdecl Movie_GetYSize(ptr)
@ cdecl Movie_SetFrameRate(ptr double)
@ cdecl Movie_SetSyncAdjust(ptr ptr long)
@ cdecl Streamer_GetSoundBuffer(ptr long)
@ cdecl Streamer_GetSoundDecodeMode(ptr)
@ cdecl Streamer_GetVideoPitch(ptr ptr ptr)
@ cdecl Streamer_InitMovie(ptr ptr long str long long)
@ cdecl Streamer_InitSound(ptr ptr long long long long long)
@ cdecl Streamer_InitStreaming(ptr ptr ptr)
@ cdecl Streamer_InitVideo(ptr ptr long long long long long long long \
			   long long ptr ptr)
@ cdecl Streamer_SetPixelFormat(ptr long \
		long long long long long long long long)
@ cdecl Streamer_SetVideoPitch(ptr long long)
@ cdecl Streamer_ShutDownMovie(ptr)
@ cdecl Streamer_ShutDownSound(ptr)
@ cdecl Streamer_ShutDownVideo(ptr)
@ cdecl Streamer_Stream(ptr ptr ptr ptr long ptr ptr ptr long)
@ cdecl Streamer_SetSoundBuffer(ptr long ptr)
@ cdecl Streamer_SetSoundDecodeMode(ptr long)
