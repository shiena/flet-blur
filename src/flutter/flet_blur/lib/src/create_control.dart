import 'package:flet/flet.dart';
import 'package:flutter_acrylic/flutter_acrylic.dart';

import 'flet_blur.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "flet_blur":
      return BlurControl(
        parent: args.parent,
        control: args.control,
        backend: args.backend,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
  () async {
    await Window.initialize();
  }();
}
