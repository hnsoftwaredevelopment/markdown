# MediaElement

## Wat is het?

Een `MediaElement` kan audio of video afspelen.

## Wanneer gebruik je het?

Gebruik een `MediaElement` wanneer media onderdeel is van je WPF-scherm.

## Basisvoorbeeld

```xaml
<MediaElement Source="video.mp4" LoadedBehavior="Manual" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Source` | Mediabestand. | `<MediaElement Source="video.mp4" />` |
| `LoadedBehavior` | Gedrag bij laden. | `<MediaElement LoadedBehavior="Manual" />` |
| `UnloadedBehavior` | Gedrag bij unload. | `<MediaElement UnloadedBehavior="Stop" />` |
| `Stretch` | Schaalgedrag. | `<MediaElement Stretch="Uniform" />` |

## Uitgebreid besproken properties

### LoadedBehavior

Met `LoadedBehavior="Manual"` bestuur je het afspelen zelf via code.

## Wat kan er binnen dit component?

Een `MediaElement` bevat normaal geen child elements.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Verwachten dat elk mediaformaat overal werkt. | Afspelen kan falen. | Controleer codec-ondersteuning op het doelapparaat. |

## Praktijkvoorbeeld

```xaml
<MediaElement Source="intro.mp4"
              LoadedBehavior="Manual"
              Stretch="Uniform" />
```

