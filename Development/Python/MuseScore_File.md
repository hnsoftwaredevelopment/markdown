MuseScore_File

Important parts of the mscx file

```xml
<museScore version="3.01">
	<Score>
        <metaTag name="arranger"></metaTag>
        <metaTag name="composer">Componist</metaTag>
        <metaTag name="copyright"></metaTag>
        <metaTag name="creationDate">2019-03-25</metaTag>
        <metaTag name="lyricist">Nummer</metaTag>
        <metaTag name="movementNumber"></metaTag>
        <metaTag name="movementTitle"></metaTag>
        <metaTag name="platform">Microsoft Windows</metaTag>
        <metaTag name="poet"></metaTag>
        <metaTag name="source"></metaTag>
        <metaTag name="translator"></metaTag>
        <metaTag name="workNumber"></metaTag>
        <metaTag name="workTitle">Titel</metaTag>
        <Part>
          <Staff id="1">
          <trackName>Tenor 1</trackName>
        </Part>
		<Staff id="1">
            <Measure>
                <Rest>
                    <durationType>quarter</durationType>
                </Rest>
                <Chord>
                    <durationType>quarter</durationType>
                    <Lyrics>
                        <text>2M1C2</text>
                    </Lyrics>
                </chord>
                <Rest>
                    <durationType>quarter</durationType>
                </Rest>
                <Chord>
                    <durationType>quarter</durationType>
                    <Lyrics>
                        <text>2M1C4</text>
                    </Lyrics>
                </chord>
            </Measure>           
            <Measure>
            <Measure> 
            <Measure>
        </Staff>
```

Get Title of Document
<MuseScore>
	<Score>
		<metaTag name="lyricist">Nummer</metaTag> + “ - ” + 
					<metaTag name="workTitle">Titel</metaTag>

Get part names
<MuseScore>
	<Score>
		<Part>
			<Staff id="1"><trackName>
			<Staff id="2"><trackName>
			<Staff id="3"><trackName>
			<Staff id="4"><trackName>

Go through score measure by measure and get the lyrics chord by chord
<MuseScore>
	<Score>
		<Staff id="1">
			<Measure> 
				<Voice><Chord><Lyrics><text>
				<Voice><Chord><Lyrics><text>
				<Voice><Chord><Lyrics><text>
				…..



[[2M1C1, 2M1C2, 2M1C3, 2M1C4], [2M2C1, 2M2C2, 2M2C3, 2M2C4], 
[2M3C1, 2M3C2, 2M3C3, 2M3C4, 2M3C5], [2M4C1, 2M4C2, 2M4C3, 2M4C4, 2M4C5]], 
[[2M1C1, 2M1C2, 2M1C3, 2M1C4, 2M1C5, 2M1C6, 2M1C7, 2M1C8], 
[2M2C1, 2M2C2, 2M2C3, 2M2C5], [2M3C1, 2M3C3], [2M4C1, 2M4C2, 2M4C3]], 
[[3M1C1, 3M1C2], [3M2C1, 3M2C3, 3M2C5, 3M2C7], [3M3C1, 3M3C2, 3M3C3, 3M3C4], 
[3M4C1, 3M4C2, 3M4C3, 3M4C4, 3M4C5, 3M4C6, 3M4C7]], 
[[[4aM1C1], [4aM2C1], [4aM3C1], [4aM4C1]],[[4bM1C1], [4bM2C1], [4bM3C1], [4bM4C1]]]

Level 1 = Lyric Line
Level 2= Staff
Level 3 = Measure

[Level1a, 
   [Level 2a, 
      [Level 3a, Level 3b], 
    Level 2b, 
      [Level 3a, Level 3b]
    ], 
 Level1b, 
    [Level 2a, 
        [Level 3a, Level 3b], 
     Level 2b, 
        [Level 3a, Level 3b]
    ]
]

```xml
<Title name='000 - Title (Composer)'>
	<LyricLine nr=1>
        <Staff name="Tenor 1">
            <Measure nr=1>
                <C1 text="2M1C1">
                <C2 text="2M1C2">
                <C3 text="2M1C3">
                <C4 text="2M1C4">
            </Measure>
            <Measure nr=2>
                <C1 text="2M2C1">
                <C2 text="2M2C2">
                <C3 text="2M2C3">
                <C4 text="2M2C4">
            </Measure>
            <Measure nr=3>
                <C1 text="2M3C1">
                <C2 text="2M3C2">
                <C3 text="2M3C3">
                <C4 text="2M3C4">
                <C5 text="2M3C5">
            </Measure>
            <Measure nr=4>
                <C1 text="2M4C1">
                <C2 text="2M4C2">
                <C3 text="2M4C3">
                <C4 text="2M4C4">
                <C5 text="2M4C5">
            </Measure>
        </Staff>
        <Staff name="Tenor 2">
            <Measure nr=1>
                <C1 text="2M1C1">
                <C2 text="2M1C2">
                <C3 text="2M1C3">
                <C4 text="2M1C4">
                <C5 text="2M1C5">
                <C6 text="2M1C6">
                <C7 text="2M1C7">
                <C8 text="2M1C8">
            </Measure>
            <Measure nr=2>
                <C1 text="2M2C1">
                <C2 text="2M2C2">
                <C3 text="2M2C3">
                <C4 text="">
                <C5 text="2M2C5">
            </Measure>
            <Measure nr=3>
                <C1 text="2M3C1">
                <C2 text="">
                <C3 text="2M3C3">
            </Measure>
            <Measure nr=4>
                <C1 text="2M4C1">
                <C2 text="2M4C2">
                <C3 text="2M4C3">
            </Measure>
        </Staff>	
        <Staff name="Bariton">
            <Measure nr=1>
                <C1 text="3M1C1">
                <C2 text="3M1C2">
            </Measure>
            <Measure nr=2>
                <C1 text="3M2C1">
                <C2 text="">
                <C3 text="3M2C3">
                <C4 text="">
                <C5 text="3M2C5">
                <C6 text="">
                <C7 text="3M2C7">
            </Measure>
            <Measure nr=3>
                <C1 text="3M3C1">
                <C2 text="3M3C2">
                <C3 text="3M3C3">
                <C4 text="3M3C4">
            </Measure>
            <Measure nr=4>
                <C1 text="3M4C1">
                <C2 text="3M4C2">
                <C3 text="3M4C3">
                <C4 text="3M4C4">
                <C5 text="3M4C5">
                <C6 text="3M4C6">
                <C7 text="3M4C7">
            </Measure>
        </Staff>
        <Staff name="Bas">
            <Measure nr=1>
                <C1 text="4aM1C1">
            </Measure>
            <Measure nr=2>
            </Measure>
            <Measure nr=3>
                <C1 text="4aM3C1">
            </Measure>
            <Measure nr=4>
                <C1 text="4aM4C1">
            </Measure>
        </Staff>
    </LyricLine>
    <LyricLine nr=1>
        <Staff name="Tenor 1">
            <Measure nr=1></Measure>
            <Measure nr=2></Measure>
            <Measure nr=3></Measure>
            <Measure nr=4></Measure>
        </Staff>
        <Staff name="Tenor 2">
            <Measure nr=1></Measure>
            <Measure nr=2></Measure>
            <Measure nr=3></Measure>
            <Measure nr=4></Measure>
        </Staff>	
        <Staff name="Bariton">
            <Measure nr=1></Measure>
            <Measure nr=2></Measure>
            <Measure nr=3></Measure>
            <Measure nr=4></Measure>
        </Staff>
        <Staff name="Bas">
            <Measure nr=1>
                <C1 text="4bM1C1">
            </Measure>
            <Measure nr=2>
            </Measure>
            <Measure nr=3>
                <C1 text="4bM3C1">
            </Measure>
            <Measure nr=4>
                <C1 text="4bM4C1">
            </Measure>
        </Staff>
    </LyricLine>
</Title>
```

